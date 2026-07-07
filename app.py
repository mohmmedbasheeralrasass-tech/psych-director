import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Psych-Director")
st.title("AI Psych-Director")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # نستخدم الموديل القياسي العام
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_idea = st.text_area("What is your video idea?")
    
    if st.button("Generate Script"):
        if user_idea:
            with st.spinner("Analyzing..."):
                try:
                    response = model.generate_content(f"Create a high-retention script for: {user_idea}")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Connection Error: {e}")
