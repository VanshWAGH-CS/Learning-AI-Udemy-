# zero shot prompting
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Method 1: Using Google AI Studio API (Recommended for development)
client = OpenAI(
    api_key="",  # Replace with your actual API key
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You are a helpful assistant who only answers Maths questions. If the query is not related to maths just say sorry and move on."

# Method 2: Alternative - use google-generativeai library (more direct)
# import google.generativeai as genai
# genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

try:
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user", 
                "content": "Explain to me how AI works"
            }
        ],
        max_tokens=1000,  # Add token limit
        temperature=0.7   # Add temperature for consistency
    )
    
    print(response.choices[0].message.content)
    
except Exception as e:
    print(f"Error occurred: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure your API key is valid")
    print("2. Check if you have internet connectivity") 
    print("3. Verify the API endpoint is correct")
    print("4. Consider using the native google-generativeai library instead")