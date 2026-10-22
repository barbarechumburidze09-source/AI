import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_instruction = """
You are an experienced senior software engineer and programming mentor. 
Explain technical concepts clearly, adapt your explanations to the user's level, and use practical examples when appropriate.
Always maintain the context of the conversation.
"""

def main():
    print("AI Technical Mentor ჩაირთო! (საუბრის დასასრულებლად ჩაწერეთ 'exit', ისტორიის სანახავად - 'history')\n")
    
    chat = client.chats.create(
        model="gemini-3.5-flash", 
        config={
            "system_instruction": system_instruction,
            "temperature": 0.5
        }
    )

    while True:
    
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
            
        if user_input.lower() == "history":
            print("\n--- Conversation History ---")
            for message in chat.get_history():
                role = "USER" if message.role == "user" else "ASSISTANT"
                print(f"{role}: {message.parts[0].text}")
            print("----------------------------\n")
            continue

        try:
            response = chat.send_message(user_input)
            print(f"\nAI: {response.text}\n")
        except Exception as e:
            print(f"\nშეცდომა: {e}\n")

if __name__ == "__main__":
    main()