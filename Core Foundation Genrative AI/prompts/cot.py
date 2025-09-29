import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# ✅ Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ System prompt to guide the chatbot
system_prompt = (
    "You are a helpful AI assistant that responds in a structured JSON format. "
    "Always reply as a JSON object with these keys:\n"
    "step: One of ['START','PLAN','OUTPUT']\n"
    "content: Your detailed answer for the current step.\n"
    "Follow this process:\n"
    "1️⃣ START → Give a short friendly greeting & ask for the user's question.\n"
    "2️⃣ PLAN → Briefly outline how you will solve the question.\n"
    "3️⃣ OUTPUT → Give the final detailed answer."
)

message_history = [
    {"role": "system", "content": system_prompt}
]

# ✅ First user message
user_query = input("Ask your question -> ")
message_history.append({"role": "user", "content": user_query})

while True:
    # 🔥 Chat loop with JSON response
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use a valid OpenAI model
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON received:", raw_result)
        break

    # ✅ Save assistant reply to history
    message_history.append({"role": "assistant", "content": raw_result})

    step = parsed_result.get("step", "").upper()
    content = parsed_result.get("content", "")

    if step == "START":
        print("🔥 START:", content)
        continue

    elif step == "PLAN":
        print("🧠 PLAN:", content)
        continue

    elif step == "OUTPUT":
        print("✅ OUTPUT:", content)
        break

# -------------------------------------------------------
# 🔢 Second model: Only answers MATH questions
# -------------------------------------------------------
math_response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful assistant who only answers Math questions. "
                "If the query is NOT related to mathematics, respond with: "
                "'Sorry, I can only answer math questions.'"
            )
        },
        {"role": "user", "content": "Explain to me how AI works"}  # Example non-math query
    ],
    max_tokens=200,
    temperature=0.7
)

print("\n🔢 Math-only Bot says:", math_response.choices[0].message.content)
