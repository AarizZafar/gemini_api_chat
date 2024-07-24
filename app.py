# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
import subprocess


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(query):    
    response = model.generate_content(query)
    return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")

submit=st.button("submit")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)