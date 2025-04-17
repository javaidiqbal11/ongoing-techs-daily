import ollama
import numpy as np
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
from faster_whisper import WhisperModel
import openai

# Constants
MILVUS_HOST = "localhost"
COLLECTION_NAME = "audio_transcriptions"

# Connect to Milvus
connections.connect("default", host=MILVUS_HOST, port="19530")

# Define Milvus Collection Schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=5000),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),  # Adjust dimension based on embedding model
]

schema = CollectionSchema(fields, description="Transcribed audio storage")
collection = Collection(COLLECTION_NAME, schema)
collection.create_index("embedding", {"index_type": "IVF_FLAT", "metric_type": "COSINE", "params": {"nlist": 128}})

# Function to transcribe audio
def transcribe_audio(audio_path):
    model = WhisperModel("small")  # Change model size if needed (tiny, base, small, medium, large)
    segments, _ = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)
    return text

# Function to generate embeddings
def get_embedding(text):
    response = ollama.embeddings(model="mistral", prompt=text)
    return np.array(response["embedding"])

# Function to store transcription
def store_transcription(text):
    embedding = get_embedding(text).tolist()
    collection.insert([[None], [text], [embedding]])
    print("Stored transcription in Milvus.")

# Function to search and answer questions
def ask_question(query):
    query_embedding = get_embedding(query).tolist()
    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
    results = collection.search([query_embedding], "embedding", search_params, limit=3, output_fields=["text"])
    
    if results[0]:
        context = " ".join(hit.entity.get("text") for hit in results[0])
        response = ollama.chat(model="mistral", messages=[{"role": "system", "content": "Answer based on context."}, 
                                                           {"role": "user", "content": f"Context: {context}\nQuestion: {query}"}])
        return response["message"]["content"]
    return "No relevant information found."

# Main Function
if __name__ == "__main__":
    audio_file = "example.wav"  # Replace with your audio file
    transcript = transcribe_audio(audio_file)
    print("Transcription:", transcript)
    store_transcription(transcript)

    # Ask a question
    question = "What was said about the topic?"
    answer = ask_question(question)
    print("Answer:", answer)
