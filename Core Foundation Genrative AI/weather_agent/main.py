import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    print("🤖 Simple Gemini Chatbot (type 'exit' to quit)")
    
    # Initialize the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a friendly and helpful assistant. Provide clear, concise, and accurate responses. Be conversational and engaging while maintaining professionalism."
    )
    
    # Start a chat session for conversation history
    chat = model.start_chat(history=[])
    
    while True:
        user_query = input("> ")

        if user_query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        try:
            response = chat.send_message(user_query)
            print(f"🤖: {response.text}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()