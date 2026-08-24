import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Resume, Job, MatchResult
from .services import (
    ats_score,
    extract_text,
    extract_skills,
    match_resume_job,
)


# =========================================================
# DASHBOARD
# =========================================================

def dashboard(request):
    resumes = Resume.objects.order_by("-created_at")[:5]
    jobs = Job.objects.order_by("-created_at")[:5]

    return render(
        request,
        "analyzer/dashboard.html",
        {
            "resumes": resumes,
            "jobs": jobs,
        },
    )


# =========================================================
# ANALYZE RESUME
# =========================================================

def analyze_resume(request):

    if request.method != "POST":
        return redirect("dashboard")

    uploaded = request.FILES.get("resume")

    if not uploaded:
        messages.error(
            request,
            "Please upload a resume."
        )

        return redirect("dashboard")

    resume = Resume.objects.create(
        name=uploaded.name.rsplit(".", 1)[0],
        file=uploaded,
    )

    try:

        # Extract resume text
        text = extract_text(resume.file.path)

        # Calculate ATS analysis
        analysis = ats_score(text)

        # Save extracted text
        resume.extracted_text = text

        # Save ATS score
        resume.ats_score = analysis["score"]

        resume.save()

    except Exception as exc:

        resume.delete()

        messages.error(
            request,
            f"Could not analyze the resume: {exc}"
        )

        return redirect("dashboard")

    return redirect(
        "analysis",
        resume_id=resume.id
    )


# =========================================================
# ANALYSIS RESULT
# =========================================================

def analysis(request, resume_id):

    resume = get_object_or_404(
        Resume,
        pk=resume_id
    )

    analysis_data = ats_score(
        resume.extracted_text or ""
    )

    return render(
        request,
        "analyzer/analysis.html",
        {
            "resume": resume,
            "analysis": analysis_data,
        },
    )


# =========================================================
# JOB LIST
# =========================================================

def jobs(request):

    jobs_queryset = Job.objects.order_by(
        "-created_at"
    )

    return render(
        request,
        "analyzer/jobs.html",
        {
            "jobs": jobs_queryset,
        },
    )


# =========================================================
# ADD JOB
# =========================================================

def add_job(request):

    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        ).strip()

        company = request.POST.get(
            "company",
            ""
        ).strip()

        description = request.POST.get(
            "description",
            ""
        ).strip()

        if not title:
            messages.error(
                request,
                "Job title is required."
            )

            return render(
                request,
                "analyzer/add_job.html"
            )

        if not description:
            messages.error(
                request,
                "Job description is required."
            )

            return render(
                request,
                "analyzer/add_job.html"
            )

        # Automatically extract required skills
        required_skills = extract_skills(
            description
        )

        Job.objects.create(
            title=title,
            company=company,
            description=description,
            required_skills=required_skills,
        )

        messages.success(
            request,
            "Job added successfully."
        )

        return redirect("jobs")

    return render(
        request,
        "analyzer/add_job.html"
    )


# =========================================================
# MATCH RESUME WITH JOBS
# =========================================================

def match_jobs(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)

    results = []

    for job in Job.objects.all():

        data = match_resume_job(
            resume.extracted_text,
            job.description,
            job.required_skills
        )

        MatchResult.objects.update_or_create(
            resume=resume,
            job=job,
            defaults={
                'similarity': data['score'],
                'matched_skills': data['matched_skills'],
                'missing_skills': data['missing_skills'],
                'recommendation': data['recommendation'],
            }
        )

        results.append((job, data))

    results.sort(
        key=lambda item: item[1]['score'],
        reverse=True
    )

    return render(
        request,
        'analyzer/matches.html',
        {
            'resume': resume,
            'results': results,
        }
    )


# =========================================================
# API - RESUME ANALYSIS
# =========================================================

def api_analyze(request):

    if request.method != "POST":

        return JsonResponse(
            {
                "error": "POST required"
            },
            status=405,
        )

    uploaded = request.FILES.get(
        "resume"
    )

    if not uploaded:

        return JsonResponse(
            {
                "error": "Resume file is required"
            },
            status=400,
        )

    temp_resume = None

    try:

        # Create temporary Resume object
        temp_resume = Resume.objects.create(
            name=uploaded.name.rsplit(
                ".",
                1
            )[0],
            file=uploaded,
        )

        # Extract text
        text = extract_text(
            temp_resume.file.path
        )

        # Analyze ATS
        result = ats_score(text)

        return JsonResponse(
            {
                "file": uploaded.name,
                "analysis": result,
            }
        )

    except Exception as exc:

        return JsonResponse(
            {
                "error": str(exc)
            },
            status=400,
        )

    finally:

        if temp_resume:

            temp_resume.delete()