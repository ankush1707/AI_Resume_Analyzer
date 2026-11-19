from resume_parser import extract_resume_text
from skills_extractor import extract_skills
from recommendations import generate_recommendations

import streamlit as st
import re


def calculate_resume_score(resume_text, extracted_skills):
    """Score resume completeness and return actionable improvement feedback."""
    text = resume_text.lower()
    score = 0
    feedback = []

    sections = (
        ("contact information", r"\b(email|phone|linkedin|github)\b", 10),
        ("professional summary or objective", r"\b(summary|objective|profile)\b", 10),
        ("work experience", r"\b(experience|employment|professional history)\b", 20),
        ("education", r"\b(education|academic|university|college)\b", 15),
        ("skills", r"\b(skills|technical skills|technologies)\b", 15),
        ("projects or certifications", r"\b(projects?|certifications?|licenses?)\b", 10),
    )

    for label, pattern, points in sections:
        if re.search(pattern, text):
            score += points
        else:
            feedback.append(f"Consider adding a clear {label} section.")

    if len(resume_text.split()) >= 150:
        score += 10
    else:
        feedback.append("Add relevant detail to give a fuller picture of your experience.")

    if re.search(r"\b\d+%|\b\d+\+?\s*(years?|users?|clients?|projects?)\b", text):
        score += 10
    else:
        feedback.append("Include measurable results to demonstrate the impact of your work.")

    if isinstance(extracted_skills, dict) and any(extracted_skills.values()):
        score += 10
    else:
        feedback.append("Highlight relevant technical and professional skills.")

    return min(score, 100), feedback

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Application title
st.title("🚀 AI Resume Analyzer")

st.write(
    "Upload your resume and analyze your "
    "skills, experience and resume quality."
)

job_description = st.text_area(
    "Paste Job Description (Optional)",
    placeholder="Paste the job requirements here...",
    height=180
)

# Sidebar
st.sidebar.title("Navigation")

menu = st.sidebar.selectbox(
    "Choose an option",
    ["Home", "Resume Analysis", "About"]
)


if menu == "Home":

    st.header("Home")

elif menu == "Resume Analysis":

    st.header("Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("Resume uploaded successfully!")

        st.write("File Name:", uploaded_file.name)

        if st.button("Analyze Resume"):

            resume_text = extract_resume_text(uploaded_file)

            if resume_text.strip():

                st.subheader("Extracted Resume Content")

                st.text_area(
                    "Resume Text",
                    resume_text,
                    height=300
                )

                # Extract technical skills
                st.subheader("Technical Skills Analysis")

                extracted_skills = extract_skills(resume_text)

                total_skills = sum(
                    len(skills)
                    for skills in extracted_skills.values()
                )

                if extracted_skills:

                    st.metric(
                        "Total Skills Identified",
                        total_skills
                    )

                    for category, skills in extracted_skills.items():

                        st.write("###", category)

                        st.write(", ".join(skills))

                    st.success("Skills extracted successfully!")

                else:

                    st.warning("No technical skills found.")

                # Calculate Resume Score
                st.subheader("Resume Score")

                score, feedback = calculate_resume_score(
                    resume_text,
                    extracted_skills
                )

                # Display score
                st.metric(
                    label="Overall Resume Score",
                    value=f"{score}/100"
                )

                # Progress bar
                st.progress(score / 100)

                # Display score interpretation
                if score >= 80:
                    st.success("Excellent Resume!")

                elif score >= 60:
                    st.info("Good Resume. Some improvements needed.")

                elif score >= 40:
                    st.warning("Average Resume. Needs improvement.")

                else:
                    st.error("Resume needs significant improvement.")

                # Display resume improvement suggestions
                st.subheader("Improvement Suggestions")

                if feedback:
                    for suggestion in feedback:
                        st.write("💡", suggestion)
                else:
                    st.success("No missing sections detected!")

                # Smart Resume Recommendations
                st.subheader("💡 Smart Recommendations")

                result = generate_recommendations(
                    resume_text,
                    extracted_skills,
                    job_description
                )

                # Display missing sections
                st.write("### Missing Resume Sections")

                if result["missing_sections"]:

                    for section in result["missing_sections"]:
                        st.warning(f"Missing: {section}")

                else:
                    st.success("All important sections detected!")

                # Display job-related missing skills
                st.write("### Job Description Skill Matching")

                if job_description.strip():

                    if result["missing_skills"]:

                        st.write("Skills to review:")

                        for skill in result["missing_skills"]:
                            st.write("🔸", skill)

                    else:
                        st.success("All detected job skills are present!")

                else:
                    st.info("Add a job description to enable skill matching.")

                # Display recommendations
                st.write("### Improvement Suggestions")

                for recommendation in result["recommendations"]:
                    st.write("💡", recommendation)

            else:
                st.warning("No readable text found in this PDF.")

