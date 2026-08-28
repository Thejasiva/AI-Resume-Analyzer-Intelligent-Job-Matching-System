# ResumeIQ — AI Resume Analyzer & Intelligent Job Matching System

<p align="center">

  <strong>Turn your resume into a career advantage.</strong>

  <br><br>

  An AI-powered web application that analyzes resumes for ATS readiness,
  extracts skills and keywords, identifies skill gaps, and intelligently
  matches candidates with relevant job opportunities.

</p>

<p align="center">

  <a href="https://resumeiq-djou.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-ResumeIQ-20C997?style=for-the-badge" alt="Live Demo">
  </a>

  <a href="https://github.com/Thejasiva/AI-Resume-Analyzer-Intelligent-Job-Matching-System">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>

</p>

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/NLP-Natural%20Language%20Processing-8A2BE2?style=flat-square">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=flat-square&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/Deployment-Render-46E3B7?style=flat-square">
  
</p>

---

## 🌐 Live Demo

### [🚀 Launch ResumeIQ](https://resumeiq-djou.onrender.com)

The application is deployed as a live Django web application using
Gunicorn and Render.

> **Note:** The application is hosted on Render's free tier, so the first
> request after a period of inactivity may take some time while the service
> starts.

---

## 📌 Overview

**ResumeIQ** is an AI-assisted career technology platform designed to help
job seekers understand how effectively their resumes communicate their
skills and how closely they match available job opportunities.

The system combines:

- Resume document processing
- Natural Language Processing (NLP)
- Skill and keyword extraction
- ATS-oriented resume evaluation
- Job description analysis
- Skill-based matching
- Semantic similarity
- Skill-gap identification
- Job relevance scoring

The goal is to transform an unstructured resume into meaningful,
actionable career insights.

---

## 🎯 Problem Statement

Modern recruitment processes frequently use Applicant Tracking Systems (ATS)
to automatically filter and rank resumes before they reach recruiters.

Job seekers may therefore face difficulties such as:

- Not knowing whether their resume is ATS-friendly
- Missing important keywords
- Not understanding which skills are relevant to a job
- Manually comparing their resume with multiple job descriptions
- Identifying skills they lack for specific roles

ResumeIQ addresses these challenges by automatically analyzing resumes and
comparing candidate profiles with job requirements.

---

## 💡 Key Features

### 📄 Resume Analysis

Upload a resume and automatically extract and analyze its textual content.

Supported formats:

- PDF
- DOCX
- TXT

The system processes the document and converts its content into structured
information for further analysis.

---

### 🤖 ATS Readiness Analysis

ResumeIQ evaluates important resume characteristics and generates an
**ATS Readiness Score**.

The analysis includes:

- Resume section detection
- Summary detection
- Experience detection
- Education detection
- Skills section detection
- Projects detection
- Contact information signals
- Professional links
- Keyword and skill coverage
- Resume content signals

The result is presented through an easy-to-understand ATS checklist and
overall readiness score.

---

### 🧠 Skill & Keyword Extraction

The system identifies relevant technical and professional skills from the
uploaded resume.

Example detected skills:

```text
Python
Django
HTML
CSS
JavaScript
React
SQL
Git
GitHub
Communication
