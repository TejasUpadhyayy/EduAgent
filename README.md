
# **AI-Powered Learning Assistant**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![QuizAPI](https://img.shields.io/badge/QuizAPI-00BFFF?style=for-the-badge&logo=api&logoColor=white)

The **AI-Powered Learning Assistant** is a Streamlit-based application designed to guide users through skill development using a structured workflow. It leverages **Google Gemini** for AI-powered learning assistance and **QuizAPI** for assessments. The application is modular, scalable, and provides a personalized learning experience.

---

## **Features**

1. **Onboarding:**
   - Collect user goals, preferred learning styles, and areas of interest.
   - Perform skill gap analysis using Gemini.

2. **Personalized Curriculum:**
   - Generate a tailored curriculum with structured lessons and milestones.
   - Dynamically adapt based on user progress.

3. **Learning Assistance:**
   - Provide real-time feedback and explanations using Gemini.
   - Interactive avatar for engaging learning experiences.

4. **Practice & Application:**
   - Offer real-world exercises and problem-solving scenarios.
   - Hands-on learning with interactive coding challenges.

5. **Assessment:**
   - Conduct quizzes and tests using QuizAPI.
   - Provide instant feedback and performance analytics.

6. **Certification:**
   - Issue certificates upon successful completion of the course.

7. **Post-Course Engagement:**
   - Recommend additional resources and challenges.
   - Keep learners engaged with updates and community forums.

---

## **Project Structure**

```
ai-learning-assistant/
│
├── .env                  # Environment variables for API keys
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
│
├── modules/
│   ├── onboarding.py     # Onboarding module
│   ├── curriculum.py     # Curriculum generation module
│   ├── learning.py       # Learning assistance module
│   ├── practice.py       # Practice and application module
│   ├── assessment.py     # Assessment module
│   ├── certification.py  # Certification module
│   └── engagement.py     # Post-course engagement module
│
├── utils/
│   ├── api_utils.py      # Utility functions for API calls
│   ├── progress_tracker.py # Progress tracking and analytics
│   └── avatar.py         # Interactive avatar for explanations
│
└── assets/               # Static files (e.g., images, certificates)
    ├── certificate_template.png
    └── avatar.png
```

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher.
- A Google Gemini API key (free tier available).
- A QuizAPI API key (free tier available).

### **2. Clone the Repository**
```bash
git clone https://github.com/your-username/ai-learning-assistant.git
cd ai-learning-assistant
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add your API keys:
```plaintext
GEMINI_API_KEY=your_gemini_api_key
QUIZAPI_API_KEY=your_quizapi_key
```

### **5. Run the Application**
```bash
streamlit run app.py
```

---

## **Usage**

1. **Onboarding:**
   - Enter your goals, preferred learning style, and skill level.
   - Complete the skill gap analysis.

2. **Curriculum:**
   - Generate a personalized curriculum based on your inputs.

3. **Learning Assistance:**
   - Ask questions and get real-time explanations from the AI assistant.
   - Interact with the avatar for a more engaging experience.

4. **Practice:**
   - Complete real-world exercises and coding challenges.

5. **Assessment:**
   - Take quizzes and tests to evaluate your progress.

6. **Certification:**
   - Receive a certificate upon course completion.

7. **Engagement:**
   - Explore additional resources and challenges to stay engaged.

---

## **APIs Used**

1. **Google Gemini:**
   - Used for skill gap analysis, curriculum generation, and learning assistance.
   - Website: [https://ai.google/](https://ai.google/)

2. **QuizAPI:**
   - Used for fetching quiz questions and conducting assessments.
   - Website: [https://quizapi.io/](https://quizapi.io/)

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- **Streamlit** for the amazing framework to build interactive web apps.
- **Google Gemini** for providing the AI capabilities.
- **QuizAPI** for the free quiz database.

---

Enjoy learning with the **AI-Powered Learning Assistant**! 🚀
