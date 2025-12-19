# Made by Vinicius Santos-Tech
# AI-POWERED INTELLIGENT SUMMARIZER

import pandas as pd
from openai import OpenAI
import streamlit as st
def read_file(file):
    while True:
        try:
            file_data = pd.read_csv(file)
            print("Loading...")
            file_content = file_data.to_string()
            client = OpenAI(api_key=''  # your_api_key_here!!!!!!!)
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions=(
                    "You will only summarize well all received files, "
                    "and do not use '*' to highlight anything."
                ),
                input=file_content
            )
            st.write(response.output_text)
            break

        except Exception as e:
            print(e)
st.title("CSV FILE SUMMARIZER!")
st.subheader(
    "Automatic tool to generate descriptions of CSV files",
    divider='blue'
)
uploaded_file = st.file_uploader(
    "Click the button to upload your CSV file",
    type=['csv']
)
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    read_file(uploaded_file)
