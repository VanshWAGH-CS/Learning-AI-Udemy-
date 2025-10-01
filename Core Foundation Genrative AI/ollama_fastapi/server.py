from fastapi import FastAPI, Body
from ollama import Client   # <-- install ollama with: pip install ollama

app = FastAPI()

# Connect to local Ollama server
client = Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(message: str = Body(..., description="User message")):
    response = client.chat(
        model="MODEL_ID",   # replace MODEL_ID with e.g. "llama2" or "mistral"
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response
