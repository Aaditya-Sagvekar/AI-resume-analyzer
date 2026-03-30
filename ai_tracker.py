import streamlit as st
import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# loading model
nlp=spacy.load("en_core_web_sm")
# extracting text from resume
def extract_resume_text(pdf_file):
    text=""
    reader=PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text+=page.extract_text()
    return text
# clean and process data
def clean_text(text):
    doc=nlp(text.lower())
    tokens=[token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)
# calculate macth score
def calculate_match(resume,jd):
    vectorizer=TfidfVectorizer()
    vectors=vectorizer.fit_transform([resume,jd])
    similarity=cosine_similarity(vectors[0:1],vectors[1:2])
    return round(similarity[0][0]*100,2)
# extract skils
domain_skills = {
    "Data Science": ["python","sql","pandas","numpy","machine learning","tableau"],
    "Marketing": ["seo","digital marketing","content marketing","social media"],
    "HR": ["recruitment","communication","hr policies","talent acquisition"]
}
def extract_skills(text,skills_list):
    found_skills=[]
    text_lower=text.lower()
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills
# STREAMLIT UI
st.title("AI Resume Analyzer & ATS Match System")
resume_file=st.file_uploader("Upload resume(PDF)",type=["pdf"])
jd_text=st.text_area("Paste internship job description here")
selected_domain=st.selectbox(
    "Select Job Domain",
    ["Data Science","Marketing","HR"]
)
if resume_file and jd_text:
    resume_text=extract_resume_text(resume_file)
    cleaned_resume=clean_text(resume_text)
    clean_jd=clean_text(jd_text)
    score=calculate_match(cleaned_resume,clean_jd)
    st.progress(int(score))
    st.subheader(f"Match score:{score}%")
    skills_list=domain_skills[selected_domain]
    resume_skills=extract_skills(resume_text)
    jd_skills=extract_skills(jd_text)
    missing_skills=list(set(jd_skills)- set(resume_skills))
# skill comparison
    st.subheader("Skills found in resume:")
    st.write(resume_skills)
    st.subheader("Missing skills")
    st.write(missing_skills)
    if missing_skills:
        st.subheader("suggestions to improve:")
        st.write(f"to increase your chances,learn: {', '.join(missing_skills)}")
    if score >=75:
        st.success("Excellent match!High chance of selection")
    elif score>=50:
        st.warning("Moderate Match.Improve some skills.")
    else:
        st.error("low match.Work on missing skills.")
    