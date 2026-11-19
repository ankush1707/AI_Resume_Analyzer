
import re


# Technical skills categorized by domain
SKILLS = {

    "Programming Languages": [
        "Python",
        "Java",
        "C++",
        "C#"
    ],

    "Databases": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "MongoDB",
        "Oracle"
    ],

    "Big Data Technologies": [
        "PySpark",
        "Spark",
        "Hadoop",
        "Hive",
        "Kafka"
    ],

    "AWS Technologies": [
        "AWS Glue",
        "Lambda",
        "S3",
        "EC2",
        "Athena",
        "Redshift"
    ],

    "Data Engineering Tools": [
        "Airflow",
        "Databricks",
        "Snowflake",
        "ETL",
        "Jenkins"
    ],

    "Other Technologies": [
        "Power BI",
        "Tableau",
        "Git",
        "Docker"
    ]
}


def extract_skills(resume_text):

    extracted_skills = {}

    # Convert text to lowercase
    resume_text = resume_text.lower()

    # Search skills category-wise
    for category, skills in SKILLS.items():

        matched_skills = []

        for skill in skills:

            # Create regex pattern
            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(skill.lower())
                + r"(?![a-z0-9])"
            )

            # Check whether skill exists
            if re.search(pattern, resume_text):

                matched_skills.append(skill)

        if matched_skills:

            extracted_skills[category] = matched_skills

    return extracted_skills
