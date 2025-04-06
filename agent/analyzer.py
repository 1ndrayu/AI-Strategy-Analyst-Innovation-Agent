from gpt4all import GPT4All
import os

# Path to your local GPT4All model
MODEL_NAME = "ggml-model-gpt4all-falcon-q4_0.bin"

def load_model():
    return GPT4All(model_name=MODEL_NAME, model_path="./", allow_download=False)

def format_prompt(text_chunks):
    joined_text = "\n".join(text_chunks)
    return f"""
You are a business strategist AI. Analyze the following user discussions, search snippets, and forum posts to identify:
1. Complaints or frustrations
2. Unmet needs or gaps in the market
3. Opportunities for innovation

Text data:
{joined_text}

Respond in bullet point format.
"""

def analyze_content(text_chunks):
    model = load_model()
    prompt = format_prompt(text_chunks)

    print("[*] Running local GPT4All model for market analysis...")
    response = model.generate(prompt, max_tokens=500, temp=0.7)

    return response.strip()
