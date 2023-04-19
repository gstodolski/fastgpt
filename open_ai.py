import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_chatgpt(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=2048)
    return response.choices[0].text.strip()
    # return "Uncomment to run chatgpt"
