import streamlit as  st
import pandas as pd 
from streamlit_extras.switch_page_button import switch_page

questions = [
    {
        #"question_id": 1,
        "question": "What aspects of your current role do you enjoy the most?",
        "question_type": "Open-ended"
    },
    {
        #"question_id": 2,
        "question": "What challenges do you face in your current position?",
        "question_type": "Open-ended"
    },
    {
        #"question_id": 3,
        "question": "How can the company support your professional development?",
        "question_type": "Open-ended"
    },
    {
        #"question_id": 4,
        "question": "Do you have any suggestions for improving communication within the team?",
        "question_type": "Open-ended"
    },
    {
        #"question_id": 5,
        "question": "How satisfied are you with the opportunities for professional growth and development?",
        "question_type": "Likert scale"
    }
]
data_2 = [{
        #"question_id": 6,
        "question": "How satisfied are you with your current role and responsibilities?",
        "question_type": "Likert scale"
    },
    {
       #"question_id": 7,
        "question": "How satisfied are you with the work-life balance provided by the company?",
        "question_type": "Likert scale"
    },
    {
        #"question_id": 8,
        "question": "Do you feel that your skills and abilities are effectively utilized in your current position?",
        "question_type": "Yes/No"
    },
    {
        #"question_id": 9,
        "question": "Do you feel you receive adequate recognition for your contributions and achievements?",
        "question_type": "Yes/No"
    },
    {
        #"question_id": 10,
        "question": "Do you feel that the company's mission and values align with your personal values?",
        "question_type": "Yes/No"
    }
]

st.header("Create form")

df = pd.DataFrame(questions)
#df.question_type = df.question_type.astype("category")
#df.question_type = df.question_type.cat.add_categories(("Open-ended", "Likert scale", "Yes/No"))

with st.form("data_editor_form"):
    st.caption("Add more questions below")
    edited_df = st.data_editor(df, num_rows="dynamic", hide_index=True, use_container_width=True)
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        switch_page("demo: user")
