import openai
import gradio as gr

# Configure OpenRouter API
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# List of Free LLMs Available on OpenRouter
models = [
    "grok-1",  # xAI (Elon Musk’s AI model)
    "deepseek-coder-33b-instruct",  # DeepSeek model for coding
    "deepseek-chat",  # DeepSeek model for conversations
    "mistral/mistral-7b-instruct",  # Mistral AI
    "mistral/mixtral-8x7b-instruct",  # Mixtral Mixture-of-Experts
    "meta/llama-3-8b-chat",  # Meta's LLaMA-3
    "meta/llama-3-70b-chat",  # Larger version of LLaMA-3
    "cohere/command-r-plus",  # Cohere's Command R+
    "openai/gpt-3.5-turbo",  # OpenAI GPT-3.5-Turbo
    "openai/gpt-4-turbo",  # OpenAI GPT-4-Turbo
    "anthropic/claude-3-haiku",  # Claude-3-Haiku (fastest Claude model)
    "qwen/qwen-vl-plus",  # Qwen VL+ (Vision-Language model)
    "openchat/openchat-7b",  # OpenChat AI model
    "mythomax/mythomax-13b",  # Mythomax AI model
    "openai/gpt-4",  # OpenAI's GPT-4
    "openai/gpt-3.5-turbo",  # OpenAI's GPT-3.5 Turbo
    "anthropic/claude-2",  # Anthropic's Claude 2
    "meta-llama/llama-2-70b-chat",  # Meta's LLaMA-2 70B Chat
    "google/gemini-1.5",  # Google's Gemini 1.5
    "cohere/command-r",  # Cohere's Command R
    "mistral/mistral-7b",  # Mistral's 7B model
    "together/llama-3.3b",  # Together's LLaMA 3.3B
    "deepseek/deepseek-13b",  # DeepSeek's 13B model
    "grok/grok-1"  # Grok's first model
]

# Function to query OpenRouter API
def chat_with_llm(model, prompt):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content  # Extracts response text
    except Exception as e:
        return f"Error: {e}"  # Display error message in the UI

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("## Chat with Multiple Free LLMs via OpenRouter API")
    
    model_dropdown = gr.Dropdown(
        choices=models,
        label="Select an LLM Model",
        value=models[0]  # Default model selected
    )
    
    input_text = gr.Textbox(label="Enter your prompt", placeholder="Type something...")
    
    output_text = gr.Textbox(label="LLM Response", interactive=False)
    
    submit_btn = gr.Button("Generate Response")

    submit_btn.click(fn=chat_with_llm, inputs=[model_dropdown, input_text], outputs=output_text)

app.launch(share=True)

