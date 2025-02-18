import streamlit as st
import requests
import os

def conduct_assessment():
    st.header("📝 Assessment")

    if 'goals' not in st.session_state:
        st.warning("Please complete the onboarding first.")
        return

    # Fetch quizzes from QuizAPI
    api_key = os.getenv("QUIZAPI_API_KEY")
    url = f"https://quizapi.io/api/v1/questions?apiKey={api_key}&limit=5"
    response = requests.get(url)

    if response.status_code == 200:
        questions = response.json()
        for i, question in enumerate(questions):
            st.write(f"**Q{i+1}: {question['question']}**")
            options = question['answers']
            user_answer = st.radio("Choose an answer:", [opt for opt in options.values() if opt is not None])
            if st.button(f"Submit Answer for Q{i+1}"):
                correct_answer = question['correct_answers']
                st.write(f"**Correct answer:** {correct_answer}")
    else:
        st.error("Failed to fetch questions. Please try again later.")