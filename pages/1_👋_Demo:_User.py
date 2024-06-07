import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.header("Your Forms")

col1, col2 = st.columns(2)
col1.write("Training and Development Form")
show1 = col2.button("Open", use_container_width=True, key="button1")
""
col1, col2 = st.columns(2)
show2 = col2.button("Open", use_container_width=True, key="button2")
col1.write("Employee Feedback Form")
""
col1, col2 = st.columns(2)
show3= col2.button("Open", use_container_width=True, key="button3")
col1.write("Work-Life Balance Survey")

if show1:
    switch_page("demo: training and development form")

if show2:
    switch_page("demo: employee feedback form")

if show3:
    switch_page("demo: work-life balance survey")