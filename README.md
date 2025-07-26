# 🧙‍♂️ AI Dungeon Story Generator

**Internship Project by:** Harsimran Singh  
**Built with:** Streamlit + Google Gemini API  
**Type:** Creative AI / Generative Text Web App  

---

## 🧾 Project Summary

As part of my AI/ML journey, I developed the **AI Dungeon Story Generator** — a web app that creates immersive, chapter-based stories using Google's Gemini (1.5 Flash) language model.

Users start with a small idea or scene — just a few lines of imagination — and the app spins it into a full-blown narrative with rich descriptions and character dialogue. Each new chapter builds **intelligently upon the previous ones**, remembering the plot, tone, and characters to maintain narrative consistency. 

This not only showcases the power of **generative AI** and **prompt engineering**, but also makes it a **powerful creative companion for aspiring young writers**, helping them bring stories to life with just a spark of an idea.

---

## ✨ Features

- 🎭 Choose from genres like **Fantasy, Mystery, Horror, Sci-Fi, Adventure**, or **Random**
- ✍️ Input a **short story prompt** — even just a single line
- 📖 Instantly generates **Chapter 1** with vivid storytelling and dialogues
- 🔁 Continue your tale by giving new prompts — it auto-generates the next chapters
- 🧠 **Remembers and builds on the previous story**, keeping flow and characters intact
- 🏷️ Auto-generates a **creative and catchy title** based on your opening chapter
- 🚀 Ideal for **young creators or beginner writers** who want to develop stories with ease

---

## 🧠 How It Works

1. **Frontend**: A clean, easy-to-use UI made in **Streamlit**, where users can input prompts and read the generated chapters.
2. **Smart Prompting Logic**:  
   - The `story_gen.py` module interacts with **Gemini API**, crafting detailed prompts for each chapter.
   - It includes the **full previous story context**, allowing Gemini to remember characters, plot points, and themes.
   - This results in smooth transitions and storytelling that feels like a single cohesive novel.
3. **Session State Memory**:  
   - The app uses `st.session_state` to keep track of the ongoing story, genre, title, and current chapter.
   - This means the app "remembers" everything you've written so far and builds directly upon it.

---

## 🛠️ Technologies Used

| Technology      | Purpose                        |
|----------------|--------------------------------|
| Python          | Core programming language      |
| Streamlit       | Frontend/UI framework          |
| Gemini API      | Story generation (LLM)         |
| dotenv          | API key and config handling    |

---

## 🎯 Outcomes

- Gained hands-on experience in **multi-turn prompt engineering**
- Built a fully functional, **context-aware AI writing assistant**
- Designed an intuitive UI for non-technical users (especially beginner writers)
- Demonstrated how LLMs can **augment human creativity**, not replace it

---

## 🌱 Potential Future Additions

- Export full stories as **PDF/ePub** for sharing or publishing
- Integrate **DALL·E or Gemini Vision** to create illustrations per chapter
- Add **save/load story sessions** using Firebase or Supabase
- Enable **branching story paths** for RPG-style choose-your-own-adventure storytelling

---

## 📬 About Me

**Harsimran Singh**  
AI/ML + Full-Stack Developer  


---

## 🏁 Final Thoughts

This project merges **tech and imagination**, helping anyone — especially young writers — to turn small ideas into epic adventures. With memory of previous chapters and guided generation, it’s like having a co-writer who never runs out of ideas ✨

**Streamlit + Gemini** gave me the perfect stack to bring this idea to life, and I’m proud to present this as part of my internship journey with **ElevateLabs** 🚀
