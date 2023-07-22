import streamlit as st
import openai
import os

from gptree import get_full_prompt
from gptree.api import call_api

import html

from dotenv import load_dotenv



load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

input_prompt = "Please evaluate the following code for bugs, errors, security flaws, poor practices, or anything else you think is worth mentioning:"


st.title('GPTree Code Evaluation')

directory = st.text_input("Directory", value=os.getcwd())
prompt = st.text_input("Prompt", value=input_prompt)
history = st.empty()
st.markdown(history)

execute_button = st.button('Evaluate')

if execute_button:
    full_prompt = get_full_prompt(prompt)
    result = call_api(full_prompt)
    
    history.markdown(result, unsafe_allow_html=True)