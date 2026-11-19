

import re


def calculate_resume_score(resume_text, extracted_skills):

    score = 0
    feedback = []

    text = resume_text.lower()

    # 1. Contact Information
    email_pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    phone_pattern = r'\b\d{10}\b'

    if re.search(email_pattern, resume_text):
        score += 5
    else:
        feedback.append("Add your email address.")

    if re.search(phone_pattern, resume_text):
        score += 5
    else:
        feedback.append("Add your contact number.")

    # 2. Professional Summary
    if "summary" in text or "objective" in text:
        score += 15
    else:
        feedback.append("Add a professional summary.")

    # 3. Technical Skills
    total_skills = sum(
        len(skills)
        for skills in extracted_skills.values()
    )

    if total_skills >= 8:
        score += 25
    elif total_skills >= 5:
        score += 18
    elif total_skills >= 3:
        score += 12
    elif total_skills >= 1:
        score += 5
    else:
        feedback.append("Add relevant technical skills.")

    # 4. Work Experience
    if "experience" in text or "employment" in text:
        score += 20
    else:
        feedback.append("Add your work experience.")

    # 5. Education
    if any(word in text for word in [
        "education", "bachelor", "master",
        "degree", "university"
    ]):
        score += 15
    else:
        feedback.append("Add educational qualifications.")

    # 6. Projects
    if "projects" in text or "project" in text:
        score += 10
    else:
        feedback.append("Add relevant projects.")

    # 7. Certifications
    if "certification" in text:
        score += 5
    else:
        feedback.append("Add relevant certifications if available.")

    return score, feedback
