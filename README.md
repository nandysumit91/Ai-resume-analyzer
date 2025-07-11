# 🤖 AI Resume Analyzer

An intelligent resume analyzer that extracts content from PDF resumes and evaluates them using Google's Gemini AI. It identifies strengths, weaknesses, and recommends relevant skills and courses for career improvement.

---

## 📌 Features

- 📄 Extracts text from both text-based and image-based resumes
- 🧠 Uses Gemini AI to:
  - Evaluate resume content
  - Suggest skills to improve
  - Recommend relevant online courses
- ✅ Supports Google Colab for free usage
- 🌐 Option to deploy with Streamlit (optional)

---

## 🚀 Demo (Colab)

> 📎 [Run on Google Colab](https://colab.research.google.com/drive/1osdkeQqoAlc7OHXQHowQMC8Bp9NslJgq#scrollTo=sI0nriOnzToL)

Just upload your resume (`Resume.pdf`) and run all cells!

---

## 🧪 Sample Output

Extracted Text from PDF:
SUMIT KUMAR NANDY
West Bengal, India | P: +xxxxxxxxxx | ...
...

Resume Evaluation:
✅ Strong in ML projects and fundamentals
⚠️ Needs improvement in resume structure and MLOps
🎯 Recommended courses: Cloud (AWS/GCP), MLOps, Advanced ML



---

## 📂 Project Structure

.
├── AI_resume_analyzer_Colab.ipynb # Google Colab notebook with full code
├── README.md # Project overview and usage guide



> 💡 All core logic is inside the Colab notebook, including PDF parsing, OCR fallback, and Gemini evaluation.

---

## 🛠️ Technologies Used

- Python
- `pdfplumber` – for direct PDF text extraction
- `pdf2image` + `pytesseract` – for OCR fallback
- Google Gemini API (`google.generativeai`)
- Streamlit (optional frontend if deployed)
- Google Colab (runtime environment)

---

## 📥 How to Use (on Colab)

1. 📁 Upload your resume to Colab (`Resume.pdf`)
2. ✅ Run all cells
3. 🧠 The model will extract text and generate an evaluation using Gemini
4. 📊 You’ll get personalized suggestions and skill recommendations

---

## 📦 Optional: Streamlit Frontend (Local)

If you'd like to run it with a simple frontend on your local machine:

```bash
pip install streamlit pdfplumber pytesseract pdf2image python-dotenv google-generativeai
streamlit run app.py
🛑 Note: You’ll need to install poppler and Tesseract-OCR locally for OCR to work.

🔐 Gemini API Key Setup
Get your API key from: Google AI Studio

In Colab:

Create a file called .env

Add: GOOGLE_API_KEY=your_api_key_here

Or use os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

🧠 Sample Prompt Sent to Gemini

You are an experienced HR with technical knowledge...
Evaluate the following resume for a role in Machine Learning...
Highlight skills, weaknesses, and recommend courses...
🙋‍♂️ Author
Sumit Kumar Nandy
📧 nandysumit91@gmail.com
🔗 LinkedIn

⭐️ Acknowledgements
Google Gemini API

OpenAI for inspiration

pdfplumber, pytesseract, streamlit open-source communities

📃 License
This project is under the MIT License – feel free to use and modify.
















