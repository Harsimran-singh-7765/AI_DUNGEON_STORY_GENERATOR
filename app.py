import streamlit as st
from story_gen import generate_story, generate_title

st.set_page_config(page_title="AI Dungeon Story Generator", page_icon="📖", layout="centered")

if "full_story" not in st.session_state:
    st.session_state.full_story = ""
if "title" not in st.session_state:
    st.session_state.title = ""
if "genre" not in st.session_state:
    st.session_state.genre = ""
if "chapter" not in st.session_state:
    st.session_state.chapter = 1

st.title("🧙‍♂️ AI Dungeon Story Generator")

with st.sidebar:
    st.header("Story Settings")
    genres = ["Fantasy", "Mystery", "Horror", "Sci-Fi", "Adventure", "Random"]
    st.session_state.genre = st.selectbox("Choose a genre:", genres)
    prompt = st.text_area("Enter the beginning of your story:", placeholder="Once upon a time...")

    if st.button("Start New Story"):
        if prompt.strip() != "":
            genre_prefix = f"Genre: {st.session_state.genre}\n" if st.session_state.genre != "Random" else ""
            full_prompt = genre_prefix + prompt
            story = generate_story(full_prompt, chapter_num=1)
            st.session_state.full_story = f"### Chapter 1\n{story}\n"
            st.session_state.title = generate_title(story)
            st.session_state.chapter = 1

if st.session_state.full_story:
    st.subheader(st.session_state.title)
    st.markdown(f"**Genre:** {st.session_state.genre}")
    st.markdown(st.session_state.full_story)

    st.subheader("Continue your story...")
    next_prompt = st.text_input("What happens next?")

    if st.button("Continue Story"):
        if next_prompt.strip() != "":
            st.session_state.chapter += 1
            continuation = generate_story(next_prompt, chapter_num=st.session_state.chapter, full_story=st.session_state.full_story)
            st.session_state.full_story += f"\n### Chapter {st.session_state.chapter}\n{continuation}\n"
