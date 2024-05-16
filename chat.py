# Example: reuse your existing OpenAI setup
from langchain_openai import OpenAI
import streamlit as st

#start the frontend server

st.title("Local- ChatGPT")


def generate_response(input_text):
    # Point to the local server
    llm = OpenAI(temperature=0.1, base_url="http://localhost:32000/v1", openai_api_key="lm-studio")
    st.info(llm(input_text))


# StreamLit Code for form

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
