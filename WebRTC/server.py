from aiohttp import web
import asyncio
import json
import numpy as np
from aiortc import RTCPeerConnection, RTCSessionDescription, MediaStreamTrack
from aiortc.contrib.media import MediaRecorder
import av

class AudioLevelTrack(MediaStreamTrack):
    kind = "audio"

    def __init__(self, track):
        super().__init__()  # initializes base MediaStreamTrack
        self.track = track

    async def recv(self):
        frame = await self.track.recv()

        # Convert audio frame to numpy array
        pcm = frame.to_ndarray()
        volume = np.sqrt(np.mean(pcm**2))
        db = 20 * np.log10(volume + 1e-6)  # avoid log(0)

        print(f"🔊 Audio level: {db:.2f} dB")

        return frame

pcs = set()

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pcs.add(pc)

    @pc.on("track")
    def on_track(track):
        if track.kind == "audio":
            print("🎙️ Audio track received")
            processed = AudioLevelTrack(track)
            recorder = MediaRecorder("/dev/null" if not hasattr(web, 'WindowsSelectorEventLoopPolicy') else "nul")
            recorder.addTrack(processed)
            asyncio.ensure_future(recorder.start())

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps({
            "sdp": pc.localDescription.sdp,
            "type": pc.localDescription.type
        })
    )

app = web.Application()
app.router.add_post("/offer", offer)

web.run_app(app, port=8080) # Select the available port for the server 

# Note: This server is a basic example and does not handle ICE candidates or other WebRTC features.
# In a production environment, you should implement ICE candidate handling and error management.
# Also, ensure you have the necessary permissions to access audio devices and record audio.


