from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client= OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Genrate a caption for this image in about 50 words"},
                {"type":"image_url", "image_url":{"url": "https://i.pinimg.com/736x/d1/9e/c3/d19ec3b32a5b95337b4f48c66f91ca6a.jpg"}}
            ]
        }
    ]
)

print("Response: ", response.choices[0].content)

