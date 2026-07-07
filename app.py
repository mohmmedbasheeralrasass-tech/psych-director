import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Director")
st.title("AI Psych-Director")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # استخدام الموديل القياسي
    model = genai.GenerativeModel('gemini-pro')
    
    idea = st.text_area("What is your video idea?")
    
    if st.button("Generate Script"):
        if idea:
            try:
                response = model.generate_content(f"Create a high-retention video script for: {idea}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
