import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import streamlit as st
from AI_CHAT import *

gemini_model = OpenAI(api_key='Enter_your_Gemini_API_KEY', base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

def chat_bot(prompt):
    mymessage = [
        {
            "role": "system",
            "content": f"You are an AI assistant. Do not suggest users to visit any website. Your duty is to provide information about all Jan Aushadhi Kendra in the nearby location the user wants and show all details of that center with their contact number : {content}"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    ai_response = gemini_model.chat.completions.create(model="gemini-2.5-flash", messages=mymessage)
    return (ai_response.choices[0].message.content)

def main():
    st.set_page_config(page_title="Jan Aushadhi Kendra Finder", layout="centered")
    st.title("Jan Aushadhi Kendra Nearby Information")
    st.write("Enter your location query below to get detailed Jan Aushadhi Kendra information without visiting any site.")

    user_query = st.text_input("Enter your location or query:", placeholder="e.g., Jan Aushadhi Kendra near Jaipur")

    if st.button("Search Kendra"):
        if user_query.strip() != "":
            with st.spinner("Fetching details, please wait..."):
                response = chat_bot(user_query)
            st.subheader("Kendra Details:")
            st.write(response)
        else:
            st.warning("Please enter a valid query to search.")

if __name__ == "__main__":

    main()
