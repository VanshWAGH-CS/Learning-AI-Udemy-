import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests
import json
import subprocess

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ------------------------------
# Tool Functions
# ------------------------------
def get_weather(city: str):
    """Get current weather for a city"""
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}"
    return "Something went wrong while fetching weather data."

def write_file(filepath: str, content: str):
    """Write content to a file"""
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filepath, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {filepath}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def run_command(cmd: str):
    """Execute a system command"""
    try:
        # Use subprocess for better control
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=30
        )
        
        output = result.stdout if result.stdout else result.stderr
        if result.returncode == 0:
            return f"✅ Command executed successfully.\nOutput: {output if output else 'No output'}"
        else:
            return f"⚠️ Command failed with code {result.returncode}.\nError: {output}"
    except subprocess.TimeoutExpired:
        return "⚠️ Command timed out after 30 seconds"
    except Exception as e:
        return f"❌ Error executing command: {str(e)}"

# Map of available tools
available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "write_file": write_file
}

# ------------------------------
# Tool Declarations for Gemini
# ------------------------------
tools = [
    genai.protos.Tool(
        function_declarations=[
            genai.protos.FunctionDeclaration(
                name="get_weather",
                description="Fetches the current weather information for a specified city. Returns temperature and weather conditions.",
                parameters=genai.protos.Schema(
                    type=genai.protos.Type.OBJECT,
                    properties={
                        "city": genai.protos.Schema(
                            type=genai.protos.Type.STRING,
                            description="The name of the city to get weather for"
                        )
                    },
                    required=["city"]
                )
            ),
            genai.protos.FunctionDeclaration(
                name="write_file",
                description="Writes content to a file. Creates directories if needed. Use this to create code files for projects.",
                parameters=genai.protos.Schema(
                    type=genai.protos.Type.OBJECT,
                    properties={
                        "filepath": genai.protos.Schema(
                            type=genai.protos.Type.STRING,
                            description="The file path where content should be written"
                        ),
                        "content": genai.protos.Schema(
                            type=genai.protos.Type.STRING,
                            description="The content to write to the file"
                        )
                    },
                    required=["filepath", "content"]
                )
            ),
            genai.protos.FunctionDeclaration(
                name="run_command",
                description="Executes a system command. Use for creating directories (mkdir), listing files (ls/dir), or other system operations. For Windows use 'dir', for Linux/Mac use 'ls'.",
                parameters=genai.protos.Schema(
                    type=genai.protos.Type.OBJECT,
                    properties={
                        "cmd": genai.protos.Schema(
                            type=genai.protos.Type.STRING,
                            description="The system command to execute"
                        )
                    },
                    required=["cmd"]
                )
            )
        ]
    )
]

# ------------------------------
# Agent Loop
# ------------------------------
def main():
    print("🤖 Agentic Gemini Chatbot (type 'exit' to quit)")
    print("💡 I can check weather, create files, and run system commands!")
    print("=" * 60)
    
    # Initialize model with function calling
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        tools=tools,
        system_instruction=(
            "You are an intelligent coding assistant that can create applications. "
            "When a user asks you to create an app or project:\n"
            "1. PLAN the project structure\n"
            "2. Use write_file to create necessary code files with complete, functional code\n"
            "3. Use run_command to create directories if needed (mkdir command)\n"
            "4. Create all files needed for a working application\n"
            "5. Provide clear instructions on how to run the app\n\n"
            "For weather queries, use get_weather.\n"
            "Always write complete, working code - no placeholders or TODOs.\n"
            "Create proper project structures with appropriate files.\n"
            "Be proactive - if user asks for a todo app, immediately start creating files."
        )
    )
    
    chat = model.start_chat(enable_automatic_function_calling=True)
    
    while True:
        user_query = input("\n> ")

        if user_query.lower() in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break

        try:
            print("\n💭 Processing your request...")
            
            # Send message to model
            response = chat.send_message(user_query)
            
            # The model will automatically call functions and return final response
            print(f"\n🤖: {response.text}")
            
        except Exception as e:
            print(f"⚠️ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()