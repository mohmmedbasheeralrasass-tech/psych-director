import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Psych-Director")
st.title("AI Psych-Director | المخرج النفسي")

api_key = st.text_input("أدخل Gemini API Key الخاص بك:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    user_idea = st.text_area("ما هي فكرة الفيديو أو موضوعه؟")
    
    if st.button("هندسة وإخراج السكريبت سيكولوجياً"):
        if user_idea:
            try:
                response = model.generate_content(f"You are an expert content director. Create a high-retention script for: {user_idea}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
