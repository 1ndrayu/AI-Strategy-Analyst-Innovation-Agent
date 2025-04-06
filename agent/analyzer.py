from gpt4all import GPT4All

MODEL_PATH = "./models/ggml-model-gpt4all-falcon-q4_0.bin"

def load_model():
    return GPT4All(model_name=MODEL_PATH, allow_download=False)

def format_prompt(posts):
    body = "\n".join(f"- {p}" for p in posts)
    return f"""
You are a market research strategist.

Analyze the following user discussions and detect:
1. Recurring problems or complaints
2. Unmet needs or frustrations
3. New opportunities for product or service innovation

Here is the input:
{body}

Output a bullet-point report.
"""

def analyze_content(posts):
    model = load_model()
    prompt = format_prompt(posts)
    return model.generate(prompt, max_tokens=500, temp=0.7).strip()
