
import streamlit as st
import random

# Sample concept and questions
questions = {
    "LCM": [
        {"q": "What is the LCM of 4 and 6?", "a": "12", "level": "easy"},
        {"q": "What is the LCM of 5 and 10?", "a": "10", "level": "easy"},
        {"q": "What is the LCM of 3, 4, and 6?", "a": "12", "level": "medium"},
        {"q": "Find the LCM of 12, 15, and 20.", "a": "60", "level": "hard"}
    ]
}

# Session State
if "accuracy" not in st.session_state:
    st.session_state.correct = 0
    st.session_state.total = 0
    st.session_state.accuracy = 0

st.set_page_config(page_title="Adaptive Quiz", layout="centered")
st.markdown("""<h1 style='text-align: center;'>Adaptive Quiz</h1>""", unsafe_allow_html=True)

# Determine level based on performance
accuracy = st.session_state.accuracy
if accuracy >= 0.8:
    level = "hard"
elif accuracy >= 0.5:
    level = "medium"
else:
    level = "easy"

# Filter by level
eligible = [q for q in questions["LCM"] if q["level"] == level]
q_data = random.choice(eligible) if eligible else random.choice(questions["LCM"])

user_input = st.text_input(f"{q_data['q']}", key="question")
if st.button("Submit"):
    st.session_state.total += 1
    if user_input.strip() == q_data["a"]:
        st.session_state.correct += 1
        st.success("Correct!")
    else:
        st.error(f"Incorrect. Correct answer: {q_data['a']}")
    st.session_state.accuracy = st.session_state.correct / st.session_state.total

st.write(f"Accuracy: {round(st.session_state.accuracy * 100)}% | Difficulty: {level.capitalize()}")
st.caption("Quiz adapts its difficulty in real time to personalize learning.")
