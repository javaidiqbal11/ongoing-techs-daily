# import the required libraries 

# import together
# import gradio as gr

# # Set your Together AI API Key
# TOGETHER_API_KEY = "6433a628c9f30935b4a00e49e70edf07ad74948e618a619e2e352d0e258e6bf5"
# together.api_key = TOGETHER_API_KEY

# # List of 10+ Supported LLMs
# # llm_models = [
# #     "meta-llama/Llama-3.3-70B-Instruct-Turbo",
# #     "mistralai/Mistral-7B-Instruct-v0.3",
# #     "deepseek-ai/deepseek-coder-33b-instruct",
# #     "Qwen/Qwen2.5-72B-Chat",
# #     "microsoft/WizardLM-2-8x22B",
# #     "meta-llama/Llama-2-13B-chat-hf",
# #     "mosaicml/mpt-7b-chat",
# #     "bigcode/starcoder",
# #     "tiiuae/falcon-40b",
# #     "togethercomputer/RedPajama-INCITE-Base-7B",
# #     "togethercomputer/CodeLlama-34B"
# # ]


# chat_models = [
    # "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    # "mistralai/Mistral-7B-Instruct-v0.3",
    # "deepseek-ai/deepseek-llm-67b-chat",
    # "Qwen/Qwen2.5-72B-Chat",
    # "microsoft/WizardLM-2-8x22B",
    # "meta-llama/Llama-2-13b-chat-hf",
    # "mosaicml/mpt-7b-chat",
    # "bigcode/starcoder",
    # "togethercomputer/RedPajama-INCITE-Base-7B",
    # "togethercomputer/CodeLlama-34B"
# ]

# # Function to generate response from selected model
# def generate_response(model_name, user_prompt, max_tokens=200, temperature=0.7):
#     if not user_prompt.strip():
#         return "Please enter a prompt."

#     try:
#         response = together.Complete.create(
#             model=model_name,
#             prompt=user_prompt,
#             max_tokens=max_tokens,
#             temperature=temperature,
#         )
#         return response['output']
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Create Gradio Web App
# with gr.Blocks() as app:
#     gr.Markdown("## Together AI - Multi-Model Chat Interface")
    
#     with gr.Row():
#         model_dropdown = gr.Dropdown(choices=chat_models, label="Choose LLM Model")
    
#     user_input = gr.Textbox(label="Enter your prompt", lines=3)
    
#     with gr.Row():
#         temp_slider = gr.Slider(0.1, 1.5, value=0.7, step=0.1, label="Temperature")
#         token_slider = gr.Slider(50, 500, value=200, step=50, label="Max Tokens")
    
#     submit_button = gr.Button("Generate Response")
    
#     output_box = gr.Textbox(label="Model Response", interactive=False)
    
#     submit_button.click(generate_response, inputs=[model_dropdown, user_input, token_slider, temp_slider], outputs=output_box)

# # Launch the Gradio Web App
# app.launch(share=True)



############
# import os
# import together
# import gradio as gr

# # Set your Together AI API Key
# together.api_key = os.getenv("6433a628c9f30935b4a00e49e70edf07ad74948e618a619e2e352d0e258e6bf5")

# # List of Supported Chat Models
# chat_models = [
#     "deepseek-ai/DeepSeek-R1-Distill-Qwen-14",
#     "Qwen/Qwen2.5-72B-Chat",
#     "meta-llama/Llama-3.3-70B-Instruct-Turbo",
#     "mistralai/Mistral-7B-Instruct-v0.3",
#     "deepseek-ai/deepseek-llm-67b-chat",
#     "Qwen/Qwen2.5-72B-Chat",
#     "microsoft/WizardLM-2-8x22B",
#     "meta-llama/Llama-2-13b-chat-hf",
#     "mosaicml/mpt-7b-chat",
#     "bigcode/starcoder",
#     "togethercomputer/RedPajama-INCITE-Base-7B",
#     "togethercomputer/CodeLlama-34B"
#     # Add other model identifiers as needed
# ]

# # Function to generate response from the selected model
# def generate_response(model_name, user_prompt, max_tokens=200, temperature=0.7):
#     if not user_prompt.strip():
#         return "Please enter a prompt."

#     try:
#         response = together.ChatCompletion.create(
#             model=model_name,
#             messages=[{"role": "user", "content": user_prompt}],
#             max_tokens=max_tokens,
#             temperature=temperature,
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Create Gradio Web App
# with gr.Blocks() as app:
#     gr.Markdown("## Together AI - Multi-Model Chat Interface")
    
#     with gr.Row():
#         model_dropdown = gr.Dropdown(choices=chat_models, label="Choose Chat Model")
    
#     user_input = gr.Textbox(label="Enter your prompt", lines=3)
    
#     with gr.Row():
#         temp_slider = gr.Slider(0.1, 1.5, value=0.7, step=0.1, label="Temperature")
#         token_slider = gr.Slider(50, 500, value=200, step=50, label="Max Tokens")
    
#     submit_button = gr.Button("Generate Response")
    
#     output_box = gr.Textbox(label="Model Response", interactive=False)
    
#     submit_button.click(
#         generate_response, 
#         inputs=[model_dropdown, user_input, token_slider, temp_slider], 
#         outputs=output_box
#     )

# # Launch the Gradio Web App
# app.launch()


# ####################
import os
import together
import gradio as gr

# Set API Key
together.api_key = os.getenv("TOGETHER_API_KEY", "6433a628c9f30935b4a00e49e70edf07ad74948e618a619e2e352d0e258e6bf5")

# List of supported chat models
chat_models = [
    "deepseek-ai/deepseek-chat",
    "Qwen/Qwen2.5-72B-Chat",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    "grok/grok-1"
]

# Function to generate response from Together AI chat models
def generate_response(model_name, user_prompt, max_tokens=200, temperature=0.7):
    if not user_prompt.strip():
        return "Please enter a valid prompt."

    try:
        response = together.Complete.create(
            model=model_name,
            prompt=user_prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response['output']
    except Exception as e:
        return f"Error: {str(e)}"

# Build Gradio Web App
with gr.Blocks() as app:
    gr.Markdown("## Together AI - Multi-Model Chat Interface")
    
    with gr.Row():
        model_dropdown = gr.Dropdown(choices=chat_models, label="Choose Chat Model", value=chat_models[0])
    
    user_input = gr.Textbox(label="Enter your prompt", lines=3, placeholder="Type your message here...")
    
    with gr.Row():
        temp_slider = gr.Slider(0.1, 1.5, value=0.7, step=0.1, label="Temperature")
        token_slider = gr.Slider(50, 500, value=200, step=50, label="Max Tokens")
    
    submit_button = gr.Button("Generate Response")
    
    output_box = gr.Textbox(label="Model Response", interactive=False)
    
    submit_button.click(generate_response, inputs=[model_dropdown, user_input, token_slider, temp_slider], outputs=output_box)

# Launch Gradio Web App
app.launch()
