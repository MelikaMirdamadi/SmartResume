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
job_rule = st.text_input("Enter the job role you are applying for (optional):")
analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")    


if analyze_button and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file is empty. Please upload a valid resume.")
            st.stop()
        
        # Create the prompt for AI analysis
        prompt = f"""
        Please analyze the following resume and provide constructive feedback:
        
        Resume Content:
        {file_content}
        
        {"Job Role: " + job_rule if job_rule else ""}
        
        Please provide feedback on:
        1. Overall structure and formatting
        2. Content quality and relevance
        3. Skills and experience presentation
        4. Areas for improvement
        5. Specific suggestions for enhancement
        """
        
        with st.spinner("Analyzing your resume..."):
            # Use Ollama with Mistral model to analyze the resume
            response = chat(
                model='mistral',  # Using Mistral model for resume analysis
                messages=[
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
            )
            
            st.success("Analysis complete!")
            st.markdown("## AI Resume Review")
            st.write(response['message']['content'])
            
    except Exception as e:
        st.error(f"An error occurred while processing your resume: {str(e)}")
        st.error("Please make sure you have Ollama installed and running, and that you have the Mistral model available.")
        st.info("To install Mistral model, run: `ollama pull mistral` in your terminal.")

elif analyze_button and not uploaded_file:
    st.warning("Please upload a resume file first.")