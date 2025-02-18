import streamlit as st
import google.generativeai as genai
import os
from utils.avatar import display_avatar

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def learning_assistance():
    st.header("🎓 Learning Assistance")

    if 'goals' not in st.session_state:
        st.warning("Please complete the onboarding first.")
        return

    # Display avatar
    display_avatar()

    # Interactive Q&A with Gemini
    user_question = st.text_input("Ask a question about your learning topic:")
    if user_question:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_question)
        st.write("**Answer:**")
        st.write(response.text)