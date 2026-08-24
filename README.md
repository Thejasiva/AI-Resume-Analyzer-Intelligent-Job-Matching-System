# ResumeIQ — AI Resume Analyzer & Intelligent Job Matching System

A production-style academic project built with **Python, Django, NLP and machine learning**. It analyzes resumes for ATS readiness and uses TF-IDF + cosine similarity + skill overlap to rank job descriptions.

## Core features
- Resume parsing: PDF, DOCX, TXT
- ATS readiness score (0–100)
- NLP skill/keyword extraction
- Section and resume-quality checks
- Job-description library
- Intelligent resume-to-job matching
- Semantic similarity score
- Skill match score
- Missing-skill / skill-gap analysis
- Personalized match recommendation
- JSON API endpoint for resume analysis
- Django admin for managing resumes, jobs and matches
- Responsive web UI

## Tech stack
**Backend:** Python, Django 5, SQLite  
**AI/NLP:** scikit-learn TF-IDF, cosine similarity, rule-based skill extraction  
**Document AI:** PyMuPDF, python-docx  
**Frontend:** HTML, CSS, Django Templates  

## Run locally

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Demo flow
1. Upload a resume from the dashboard.
2. Review the ATS score, detected skills and section checklist.
3. Open **Jobs → Add Job** and paste real job descriptions.
4. Return to the analyzed resume and click **Match with Jobs**.
5. Review ranked matches, matched skills, missing skills and recommendations.

## API
`POST /api/analyze/` with multipart form field `resume`.

Example response:
```json
{
  "file": "resume.pdf",
  "analysis": {
    "score": 82,
    "skills": ["python", "django", "react"],
    "sections": {"summary": 1, "experience": 1, "education": 1, "skills": 1, "projects": 1},
    "word_count": 512
  }
}
```

## How the AI matching works
1. Extract text from the resume and job description.
2. Normalize and tokenize text.
3. Extract known technical and soft skills.
4. Convert resume + job text into TF-IDF vectors using uni/bi-grams.
5. Calculate cosine similarity for semantic textual overlap.
6. Calculate skill coverage from required skills.
7. Combine scores: **65% semantic similarity + 35% skill coverage**.
8. Generate a recommendation and skill-gap list.

## Recommended final-year upgrades
For a stronger MCA final-year project, add:
- spaCy NER for names, organizations, dates and education entities
- sentence-transformers embeddings for stronger semantic matching
- PostgreSQL + user authentication
- recruiter dashboard and candidate ranking
- resume section classification
- job recommendations based on multiple jobs
- explainable AI: show exactly why a match received its score
- charts for ATS trends and skill gaps
- LLM-powered resume rewriting with a provider API
- evaluation dataset with precision/recall, MAE and ranking metrics
- Docker deployment and CI/CD

## Project structure
```text
ai_resume_job_matcher/
├── analyzer/
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/analyzer/
│   └── static/analyzer/
├── resume_analyzer/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

> This is designed as a strong baseline. For a thesis-grade system, evaluate the matching model on a labeled resume/job dataset rather than treating the score as a hiring decision.
