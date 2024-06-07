import streamlit as  st 
from streamlit_extras.switch_page_button import switch_page
        
questions = [
    {
        "question_id": 1,
        "question": "How do you prioritize your work and personal life responsibilities?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 2,
        "question": "What strategies do you use to manage stress from work?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 3,
        "question": "How does the company support your need for a healthy work-life balance?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 4,
        "question": "Do you feel you have enough flexibility in your work schedule?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 5,
        "question": "How often do you find yourself working outside of regular business hours?",
        "question_type": "Likert scale (Very Often, Often, Sometimes, Rarely, Never)"
    },
    {
        "question_id": 6,
        "question": "How satisfied are you with the company's remote work policies?",
        "question_type": "Likert scale (Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied)"
    },
    {
        "question_id": 7,
        "question": "Do you feel encouraged to take breaks and use your vacation time?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 8,
        "question": "How well does your current workload allow you to maintain a healthy work-life balance?",
        "question_type": "Likert scale (Very Well, Well, Neutral, Poorly, Very Poorly)"
    },
    {
        "question_id": 9,
        "question": "What improvements could be made to enhance your work-life balance?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 10,
        "question": "Do you feel your work-life balance has improved, stayed the same, or worsened over the past year?",
        "question_type": "Multiple choice (Improved, Stayed the same, Worsened)"
    }
]


def main():
    
    if st.button("Go back"):
        switch_page("demo: user")
    
    st.header("Work-Life Balance Survey")

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