import streamlit as st
from story_gen import generate_story

st.set_page_config(page_title="AI Dungeon Story Generator", page_icon="📖")

st.title("🧙‍♂️ AI Dungeon Story Generator")
st.write("Create your own interactive story using Google's Gemini AI!")

# Initialize session state for story
if "full_story" not in st.session_state:
    st.session_state.full_story = ""


genres = ["Fantasy", "Mystery", "Horror", "Sci-Fi", "Adventure", "Random"]
genre = st.selectbox("Choose a genre for your story:", genres)


prompt = st.text_area("Enter the beginning of your story:", placeholder="Once upon a time...")


if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a story prompt to begin.")
    else:
        with st.spinner("Generating story..."):
            full_prompt = f"Genre: {genre}\n{prompt}" if genre != "Random" else prompt
            story = generate_story(full_prompt)
            st.session_state.full_story = story  
        
        st.subheader("Generated Story:")
        st.write(st.session_state.full_story)


if st.session_state.full_story:
    st.subheader("Continue your story...")
    next_prompt = st.text_input("Add something to continue the story:")

    if st.button("Continue Story"):
        if next_prompt.strip() == "":
            st.warning("Please add some text to continue.")
        else:
            with st.spinner("Generating continuation..."):
                combined_prompt = st.session_state.full_story + "\n" + next_prompt
                continuation = generate_story(combined_prompt)
                
                
                st.session_state.full_story += "\n" + continuation
            
            st.subheader("Updated Story:")
            st.write(st.session_state.full_story)
