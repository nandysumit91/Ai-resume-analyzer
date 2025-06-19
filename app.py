import streamlit as st
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini model
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("❌ GOOGLE_API_KEY not found in environment variables.")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if text.strip():
            return text.strip()
    except Exception as e:
        st.warning(f"Direct text extraction failed: {e}")

    st.info("Falling back to OCR for image-based PDF.")
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"
    except Exception as e:
        st.error(f"OCR failed: {e}")
    return text.strip()

# Function to analyze the resume using Gemini
def analyze_resume(resume_text, job_description=None):
    if not resume_text:
        return "❌ Resume text is required."

    base_prompt = f"""
    You are an experienced HR with Technical Experience in the field of one job role such as Data Science, DevOps, AI Engineer, Full Stack Developer, etc.
    Review the provided resume and share:
    - Professional evaluation
    - Existing skills
    - Missing skills
    - Suggested courses
    - Strengths and weaknesses

    Resume:
    {resume_text}
    """

    if job_description:
        base_prompt += f"\n\nJob Description:\n{job_description}\n"

    response = model.generate_content(base_prompt)
    return response.text.strip()

# Streamlit UI
st.title("📄 AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])
job_desc = st.text_area("📝 Optional: Paste Job Description")

if uploaded_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    extracted_text = extract_text_from_pdf("uploaded_resume.pdf")

    if extracted_text:
        st.subheader("📌 Extracted Resume Text")
        st.text_area("Resume Text", extracted_text, height=200)

        if st.button("🔍 Analyze Resume"):
            with st.spinner("Analyzing resume..."):
                analysis_result = analyze_resume(extracted_text, job_desc)
                st.subheader("📊 Resume Analysis Result")
                st.markdown(analysis_result)
    else:
        st.warning("❗ Could not extract any text from the uploaded PDF.")
