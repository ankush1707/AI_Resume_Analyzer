# AI Resume Analyzer 🚀

A Python-based web application that analyzes PDF resumes, extracts technical skills, calculates resume scores, identifies missing sections, and provides improvement recommendations.

## 📌 Project Overview

The AI Resume Analyzer helps users evaluate their resumes and identify areas for improvement.

Users can upload a PDF resume and optionally provide a job description. The application extracts resume content, identifies technical skills, evaluates resume sections, and provides relevant recommendations.

## ✨ Key Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Text Extraction:** Extract resume content using PyPDF.
- **Technical Skills Extraction:** Identify programming languages, databases, Big Data technologies and cloud skills using Regular Expressions.
- **Resume Scoring:** Calculate a score out of 100 based on seven resume criteria.
- **Missing Section Detection:** Identify missing professional summaries, experience, education and project sections.
- **Job Description Matching:** Compare technical skills in the resume with skills required in a job description.
- **Improvement Recommendations:** Generate suggestions to improve resume content.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF
- Regular Expressions (Regex)
- Pandas

## 📂 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── resume_parser.py
├── skills_extractor.py
├── resume_scorer.py
├── recommendations.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd AI_Resume_Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📊 Resume Scoring Criteria

The application evaluates resumes using the following criteria:

| Criteria | Maximum Score |
|---|---:|
| Contact Information | 10 |
| Professional Summary | 15 |
| Technical Skills | 25 |
| Work Experience | 20 |
| Education | 15 |
| Projects | 10 |
| Certifications | 5 |
| **Total** | **100** |

## 🔍 Application Workflow

1. Upload a PDF resume.
2. Extract resume content using PyPDF.
3. Identify technical skills using Regex.
4. Calculate the resume score.
5. Identify missing resume sections.
6. Optionally enter a job description.
7. Compare resume skills with job requirements.
8. Display improvement recommendations.

## ⚠️ Current Limitations

- Supports text-based PDF resumes; scanned PDFs require OCR.
- Skills are identified through predefined keyword matching.
- Resume scoring uses rule-based criteria and is not an official ATS score.
- Job matching currently focuses on predefined technical skills.
- Recommendations are generated using predefined Python rules.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and modular development.
- PDF processing and text extraction.
- Regular expressions and pattern matching.
- Python dictionaries, lists and functions.
- Streamlit web application development.
- Rule-based scoring and recommendation systems.
- Integrating multiple Python modules into one application.

## 👨‍💻 Author

**Ankush Chaudhari**

GitHub: Add your GitHub profile link

LinkedIn: Add your LinkedIn profile link

---

*Built as a practical Python development project to explore resume analysis and automation.*
