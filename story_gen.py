import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key not found! Please set GEMINI_API_KEY in .env file.")


genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_story(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# For testing directly from terminal
if __name__ == "__main__":
    print("Welcome to AI Dungeon Story Generator!")
    user_prompt = input("\nStart your story (e.g., 'Once upon a time...'):\n")
    
    generated_story = generate_story(user_prompt)
    
    print("\nGenerated Story:\n")
    print(generated_story)
