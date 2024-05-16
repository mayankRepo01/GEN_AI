# Example: reuse your existing OpenAI setup
from langchain_community.llms import HuggingFaceHub
from langchain_openai import OpenAI
import streamlit as st

#start the frontend server

st.title("Hugging Face - falcon-7b Model")

huggingfacehub_api_token = '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'


def generate_response(input_text):
    # Point to the local server
    llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token, model_kwargs={"temperature": 0.1})
    # llm = HuggingFaceHub(repo_id="huggingfaceh4/zephyr-7b-alpha",model_kwargs={"temperature": 0.1, "max_length": 500,"max_new_tokens":512}, huggingfacehub_api_token=huggingfacehub_api_token)


    st.info(llm(input_text))


# StreamLit Code for form

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is Gen AI')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
