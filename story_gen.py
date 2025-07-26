import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_story(prompt, chapter_num=1, full_story=None):
    if chapter_num == 1:
        final_prompt = (
            f"Generate Chapter 1 of an interactive story in a narrative style with character dialogues. "
            f"The story should be engaging, descriptive, and immersive.\nPrompt:\n{prompt}"
        )
    else:
        final_prompt = (
            f"Continue the story as Chapter {chapter_num}, keeping the narrative and dialogue-rich style consistent. "
            f"Maintain the story's flow, character development, and excitement.\n"
            f"Story so far:\n{full_story}\n\n"
            f"What happens next:\n{prompt}"
        )

    response = model.generate_content(final_prompt)
    return response.text.strip()

def generate_title(story):
    title_prompt = (
        f"Based on the following story, suggest an engaging short, creative title. "
        f"ONLY provide the title, no explanations, no list format.\n{story}"
    )
    response = model.generate_content(title_prompt)
    return response.text.strip().replace('"', '')
