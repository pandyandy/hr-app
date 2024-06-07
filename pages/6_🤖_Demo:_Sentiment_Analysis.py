import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

dummy_responses = {
    1: {
        "positive": "I genuinely enjoy the opportunity to work on diverse projects and the autonomy given in my role. Each project presents a unique challenge, which keeps my work engaging and intellectually stimulating.",
        "neutral": "I enjoy some aspects of my role, like working with my team and handling various tasks.",
        "negative": "Honestly, there isn't much that I enjoy about my current role. The tasks are repetitive and uninteresting."
    },
    2: {
        "positive": "Challenges are part of growth, and I appreciate the learning opportunities they bring. Time management is tricky, but I'm improving.",
        "neutral": "I face typical challenges like managing deadlines and balancing workload.",
        "negative": "The main challenge is the overwhelming workload and lack of support, which leads to constant stress."
    },
    3: {
        "positive": "The company can support my professional development by offering more training programs and mentorship opportunities.",
        "neutral": "Some more training programs could help, but it's not a major issue.",
        "negative": "There is very little support for professional development. More training and mentorship programs are desperately needed."
    },
    4: {
        "positive": "Improving communication within the team can be achieved by holding regular team meetings and using collaborative tools.",
        "neutral": "Regular meetings might help improve communication.",
        "negative": "Communication is a mess. Regular meetings and better tools are necessary to fix this."
    },
    5: {
        "very_satisfied": "Very Satisfied",
        "satisfied": "Satisfied",
        "neutral": "Neutral",
        "dissatisfied": "Dissatisfied",
        "very_dissatisfied": "Very Dissatisfied"
    },
    6: {
        "very_satisfied": "Very Satisfied",
        "satisfied": "Satisfied",
        "neutral": "Neutral",
        "dissatisfied": "Dissatisfied",
        "very_dissatisfied": "Very Dissatisfied"
    },
    7: {
        "very_satisfied": "Very Satisfied",
        "satisfied": "Satisfied",
        "neutral": "Neutral",
        "dissatisfied": "Dissatisfied",
        "very_dissatisfied": "Very Dissatisfied"
    },
    8: {
        "yes": "Yes",
        "no": "No"
    },
    9: {
        "yes": "Yes",
        "no": "No"
    },
    10: {
        "yes": "Yes",
        "no": "No"
    }
}

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score['compound']

def sentiment_analysis_page():
    st.header("Sentiment Analysis of Survey Responses")

    expanders = [
        ("John Doe", "June 1, 2024"),
        ("Jane Smith", "June 2, 2024"),
        ("Alice Johnson", "June 3, 2024"),
        ("Bob Brown", "June 4, 2024")
    ]

    sentiments = [
        ["positive", "positive", "positive", "positive", "very_satisfied", "very_satisfied", "very_satisfied", "yes", "yes", "yes"],
        ["neutral", "neutral", "neutral", "neutral", "satisfied", "satisfied", "satisfied", "yes", "yes", "yes"],
        ["negative", "negative", "negative", "negative", "dissatisfied", "dissatisfied", "dissatisfied", "no", "no", "no"],
        ["positive", "neutral", "positive", "neutral", "very_satisfied", "neutral", "satisfied", "yes", "yes", "no"]
    ]

    responses = []

    for (name, date), sentiment in zip(expanders, sentiments):
        respondent_data = {"name": name, "date": date}
        for i, q in enumerate(questions):
            response = dummy_responses[q["question_id"]][sentiment[i]]
            respondent_data[f"Q{q['question_id']}"] = analyze_sentiment(response)
        responses.append(respondent_data)

    df = pd.DataFrame(responses)
    def sentiment_color(sentiment):
        if sentiment > 0.2:
            return "color: #28a745"  # Green for Positive
        elif -0.2 <= sentiment <= 0.2:
            return "color: #d4b106"  # Dark Yellow for Neutral
        else:
            return "color: #dc3545" 
        
    st.dataframe(df.style.applymap(
            sentiment_color, subset=[
    "Q1",
    "Q2",
    "Q3",
    "Q4",
    "Q5",
    "Q6",
    "Q7",
    "Q8",
    "Q9",
    "Q10"
]
        ), hide_index=True, use_container_width=True)

    # Visualize sentiment with Plotly
    df_melted = df.melt(id_vars=["name", "date"], var_name="Question", value_name="Sentiment")

    fig = px.bar(df_melted, x="Question", y="Sentiment", color="Sentiment", 
                 barmode="group", facet_col="name", title="Sentiment Analysis of Survey Responses")
    
    st.plotly_chart(fig)
    
    if st.button("Send Results"):
        switch_page("demo: send results")

if __name__ == "__main__":
    sentiment_analysis_page()