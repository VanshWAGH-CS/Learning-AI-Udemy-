from google import genai

client = genai.Client(
    api_key=""
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="You only answer Math questions. if the question is not of math say sorry to the user",
    contents="Explain how AI works in a few words"
)
print(response.text)