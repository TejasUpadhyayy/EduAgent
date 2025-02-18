import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def onboarding():
    st.header("🚀 Onboarding")
    st.write("Welcome to the AI-Powered Learning Assistant! Let's get started.")

    # Step 1: Collect user goals
    goals = st.text_area("What skills do you want to develop? (e.g., Python, Data Science, Public Speaking)")
    learning_style = st.selectbox("How do you prefer to learn?", ["Reading", "Videos", "Audio", "Interactive"])
    time_commitment = st.slider("How much time can you dedicate per week (in hours)?", 1, 20)
    skill_level = st.selectbox("What is your current skill level?", ["Beginner", "Intermediate", "Advanced"])

    # Step 2: Skill gap analysis using Gemini
    if st.button("Analyze My Skill Gaps"):
        if goals:
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Analyze the skill gaps for someone who wants to learn {goals} at a {skill_level} level."
            response = model.generate_content(prompt)
            st.session_state['skill_gaps'] = response.text
            st.success("Skill gap analysis complete!")
            st.write("**Skill Gaps:**")
            st.write(response.text)
        else:
            st.warning("Please enter your goals first.")

    # Step 3: Save user data
    if st.button("Complete Onboarding"):
        st.session_state['goals'] = goals
        st.session_state['learning_style'] = learning_style
        st.session_state['time_commitment'] = time_commitment
        st.session_state['skill_level'] = skill_level
        st.success("Onboarding complete! Navigate to Curriculum to see your personalized plan.")