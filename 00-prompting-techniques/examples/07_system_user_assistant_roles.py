"""
Prompting Techniques
Example: System, User, and Assistant/Model roles
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent / "module-01-guidelines"))

from google.genai import types
from helper import get_completion


system_instruction = """
You are a beginner-friendly driving instructor.
Explain things in a simple, calm, step-by-step way.
Keep the answer clear, practical, and easy to understand.
Use a slightly fun tone, but do not become silly.
"""

user_message = "Teach me how to drive a car for the first time."

response = get_completion(
    prompt=user_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=400,
    ),
)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response)