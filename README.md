# 🚀 AI Resume Analyzer & ATS Match System

## 📌 Description
This is a web-based application built using Streamlit that analyzes resumes against job descriptions using NLP techniques. 
It calculates a match score and provides suggestions to improve the resume.

---

## 🎯 Features
- Upload resume in PDF format
- Paste job description
- Match score calculation using NLP
- Skill extraction based on job domain
- Missing skills identification
- Suggestions to improve resume
- Multi-domain support (Data Science, Marketing, HR)

---

## 🛠️ Tech Stack
- Python
- Streamlit
- spaCy (Natural Language Processing)
- scikit-learn (TF-IDF, Cosine Similarity)
- PyPDF2 (PDF processing)

---

## ⚙️ How It Works
1. Extracts text from resume PDF
2. Cleans text using NLP techniques
3. Converts text into numerical vectors using TF-IDF
4. Compares resume with job description using cosine similarity
5. Calculates match score and identifies missing skills

---

## ▶️ How to Run Locally
```bash
streamlit run ai_tracker.py
