import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_curriculum():
    st.header("📚 Personalized Curriculum")

    if 'goals' not in st.session_state:
        st.warning("Please complete the onboarding first.")
        return

    # Generate curriculum using Gemini
    if st.button("Generate Curriculum"):
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Create a {st.session_state['time_commitment']}-week curriculum for learning {st.session_state['goals']} at a {st.session_state['skill_level']} level. Include milestones and resources."
        response = model.generate_content(prompt)
        st.session_state['curriculum'] = response.text
        st.success("Curriculum generated!")

    # Display curriculum
    if 'curriculum' in st.session_state:
        st.write("**Your Curriculum:**")
        st.write(st.session_state['curriculum'])