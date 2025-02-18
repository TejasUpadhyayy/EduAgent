import streamlit as st
from dotenv import load_dotenv
import os
from modules.onboarding import onboarding
from modules.curriculum import generate_curriculum
from modules.learning import learning_assistance
from modules.practice import practice_exercises
from modules.assessment import conduct_assessment
from modules.certification import issue_certificate
from modules.engagement import post_course_engagement

# Load environment variables
load_dotenv()

# Main app
def main():
    st.title("AI-Powered Learning Assistant")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Onboarding", "Curriculum", "Learning", "Practice", "Assessment", "Certification", "Engagement"])

    if page == "Onboarding":
        onboarding()
    elif page == "Curriculum":
        generate_curriculum()
    elif page == "Learning":
        learning_assistance()
    elif page == "Practice":
        practice_exercises()
    elif page == "Assessment":
        conduct_assessment()
    elif page == "Certification":
        issue_certificate()
    elif page == "Engagement":
        post_course_engagement()

if __name__ == "__main__":
    main()