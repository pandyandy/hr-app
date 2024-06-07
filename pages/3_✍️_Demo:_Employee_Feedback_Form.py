import streamlit as  st 
from streamlit_extras.switch_page_button import switch_page
        
questions = [
    {
        "question_id": 1,
        "question": "What aspects of your current role do you enjoy the most?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 2,
        "question": "What challenges do you face in your current position?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 3,
        "question": "How can the company support your professional development?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 4,
        "question": "Do you have any suggestions for improving communication within the team?",
        "question_type": "Open-ended"
    },
    {
        "question_id": 5,
        "question": "How satisfied are you with the opportunities for professional growth and development?",
        "question_type": "Likert scale (Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied)"
    },
    {
        "question_id": 6,
        "question": "How satisfied are you with your current role and responsibilities?",
        "question_type": "Likert scale (Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied)"
    },
    {
        "question_id": 7,
        "question": "How satisfied are you with the work-life balance provided by the company?",
        "question_type": "Likert scale (Very Satisfied, Satisfied, Neutral, Dissatisfied, Very Dissatisfied)"
    },
    {
        "question_id": 8,
        "question": "Do you feel that your skills and abilities are effectively utilized in your current position?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 9,
        "question": "Do you feel you receive adequate recognition for your contributions and achievements?",
        "question_type": "Yes/No"
    },
    {
        "question_id": 10,
        "question": "Do you feel that the company's mission and values align with your personal values?",
        "question_type": "Yes/No"
    }
]

def main():
    
    if st.button("Go back"):
        switch_page("demo: user")
    
    st.header("Employee Feedback Form")

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