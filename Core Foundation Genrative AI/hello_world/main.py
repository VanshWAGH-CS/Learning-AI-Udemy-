from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    message=[
        {"role": "user", "content": "hey there"}
    ]
)

print(response.choices[0].message.content)