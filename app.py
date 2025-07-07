import streamlit as st 
from story_gen import generate_story

st.set_page_config(page_title="AI DUNGEON STORY GENERATOR")

st.title(" AI DUNGEON STORY GENERATOR ")

st.write("Create your own interactive story using Google's Gemini AI!")

# User input
prompt = st.text_area("Enter the beginning of your story:", placeholder="Once upon a time...")

# Button to generate story
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a story prompt to begin.")
    else:
        with st.spinner("Generating story..."):
            story = generate_story(prompt)
        
        st.subheader("Generated Story:")
        st.write(story)