import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# ✅ Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Persona-based system prompt
SYSTEM_PROMPT = """
You are an AI persona assistant named Vansh Wagh.
You are acting on behalf of Vansh, a 21-year-old BTech engineering student
who is currently learning Generative AI. 
You talk in a friendly, enthusiastic, and curious way—just like Vansh would.
"""

# ✅ Chat completion call
response = client.chat.completions.create(
    model="gpt-4o",  # Valid OpenAI model
    response_format={"type": "json_object"},  # Ensures clean JSON output
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey there!"}
    ]
)

# ✅ Extract and print
raw_result = response.choices[0].message.content
try:
    parsed = json.loads(raw_result)   # If model outputs JSON
    print(parsed)
except json.JSONDecodeError:
    print(raw_result)  # If it’s just text
