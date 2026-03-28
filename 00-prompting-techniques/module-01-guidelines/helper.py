import os
from dotenv import load_dotenv, find_dotenv
from google import genai

load_dotenv(find_dotenv())

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_completion(prompt, model="gemini-2.5-flash", **kwargs):
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        **kwargs
    )
    return response.text