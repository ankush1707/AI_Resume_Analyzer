
from skills_extractor import extract_skills


def generate_recommendations(
    resume_text,
    extracted_skills,
    job_description=""
):

    recommendations = []

    text = resume_text.lower()

    # 1. Check missing resume sections

    required_sections = {
        "Professional Summary": ["summary", "objective"],
        "Work Experience": ["experience", "employment"],
        "Education": ["education", "qualification"],
        "Projects": ["project", "projects"]
    }

    missing_sections = []

    for section, keywords in required_sections.items():

        if not any(keyword in text for keyword in keywords):

            missing_sections.append(section)

            recommendations.append(
                f"Add a {section} section to your resume."
            )

    # 2. Check technical skills

    if not extracted_skills:

        recommendations.append(
            "Add relevant technical skills to your resume."
        )

    # 3. Professional summary suggestions

    if "summary" not in text and "objective" not in text:

        recommendations.append(
            "Write a professional summary highlighting "
            "your experience and key strengths."
        )

    else:

        recommendations.append(
            "Keep your professional summary concise "
            "and focused on measurable achievements."
        )

    # 4. Job description matching

    missing_skills = []

    if job_description.strip():

        job_skills = extract_skills(job_description)

        resume_skill_names = {
            skill.lower()
            for skills in extracted_skills.values()
            for skill in skills
        }

        for category, skills in job_skills.items():

            for skill in skills:

                if skill.lower() not in resume_skill_names:

                    missing_skills.append(skill)

        if missing_skills:

            recommendations.append(
                "Review these job-related skills and add "
                "them only if you genuinely have experience: "
                + ", ".join(missing_skills)
            )

        else:

            recommendations.append(
                "Your resume contains all the detected "
                "technical skills from this job description."
            )

    # 5. Return results

    return {
        "missing_sections": missing_sections,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }
