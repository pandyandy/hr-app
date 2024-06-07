import streamlit as  st
import os 
import base64
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide")

image_path = os.path.dirname(os.path.abspath(__file__))

keboola_logo = image_path+"/static/csas_logo_v2.png"
logo_html = f'<div style="display: flex; justify-content: flex-end;"><img src="data:image/png;base64,{base64.b64encode(open(keboola_logo, "rb").read()).decode()}" style="width: 150px; margin-bottom: 10px;"></div>'
st.markdown(f"{logo_html}", unsafe_allow_html=True)
""
col1, col2 = st.columns(2)

if col1.button("Create form", use_container_width=True):
    switch_page("demo: create form")

if col2.button("See forms",  use_container_width=True):
    switch_page("demo: user")