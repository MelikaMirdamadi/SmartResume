import streamlit as st
import PyPDF2
import io
from ollama import chat



st.set_page_config(page_title="AI Resume Reviewer", page_icon="📝" , layout="centered")

st.title("AI Resume Reviewer📝")
st.markdown("""
Upload your resume in PDF format, and let our AI reviewer provide you with feedback to help you improve it! 
""")

uploaded_file=st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf" , "txt"])

