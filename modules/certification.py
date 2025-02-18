import streamlit as st

def issue_certificate():
    st.header("🏆 Certification")

    if 'goals' not in st.session_state:
        st.warning("Please complete the onboarding first.")
        return

    st.write("Congratulations! You've completed the course.")
    st.write("Here's your certificate:")
    st.image("assets/certificate_template.png", use_column_width=True)