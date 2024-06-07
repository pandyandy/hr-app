import streamlit as  st 
from streamlit_extras.switch_page_button import switch_page
        
questions = [
    {
        "question_id": 1,
        "question": "What new skills or knowledge would you like to acquire in the next year?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 2,
        "question": "What motivates you to perform your best at work?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 3,
        "question": "How do you prefer to receive feedback on your performance?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 4,
        "question": "What type of training or workshops would you find most beneficial?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 5,
        "question": "How would you rate the effectiveness of the current training programs?",
        "question_type": "Likert scale (Very Effective, Effective, Neutral, Ineffective, Very Ineffective)"
    },
    {
        "question_id": 6,
        "question": "How satisfied are you with the level of support you receive from your manager?",
        "question_type": "Likert scale (Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied)"
    },
    {
        "question_id": 7,
        "question": "How well do you feel your team collaborates on projects?",
        "question_type": "Likert scale (Very Well, Well, Neutral, Poorly, Very Poorly)"
    },
    {
        "question_id": 8,
        "question": "Do you have opportunities to apply what you learn in training to your job?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 9,
        "question": "Do you believe that the company provides adequate resources for professional growth?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 10,
        "question": "Do you feel that your career goals are supported by the company?",
        "question_type": "Yes/No"
    }
]


def main():
    
    if st.button("Go back"):
        switch_page("demo: user")
    
    st.header("Training and Development Form")

    responses = {}

    for q in questions:

        if q["question_type"] == "Open-ended":
            response = st.text_input(f"{q['question']}", key=q["question_id"])
        elif q["question_type"] == "Yes/No":
            response = st.radio(f"{q['question']}", ["Yes", "No"], key=q["question_id"], horizontal=True)
        elif "Likert scale" in q["question_type"]:
            options = q["question_type"].split("(")[1].replace(")", "").split(", ")
            response = st.selectbox(f"{q['question']}", options, key=q["question_id"])
        ""
        responses[q["question_id"]] = response

    if st.button("Submit"):
        switch_page("demo: responses")

if __name__ == "__main__":
    main()