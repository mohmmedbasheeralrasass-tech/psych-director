import streamlit as st
import google.generativeai as genai

st.title("AI Psych-Director")
api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    idea = st.text_area("Video Idea:")
    if st.button("Generate"):
        try:
            response = model.generate_content(idea)
            st.markdown(response.text)
        except Exception as e:
            st.error(str(e))
