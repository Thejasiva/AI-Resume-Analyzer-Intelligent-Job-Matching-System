from django.urls import path

from . import views


urlpatterns = [

    # Dashboard
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # Resume upload / analysis
    path(
        "analyze/",
        views.analyze_resume,
        name="analyze"
    ),

    # Resume analysis result
    path(
        "analysis/<int:resume_id>/",
        views.analysis,
        name="analysis"
    ),

    # Job listing
    path(
        "jobs/",
        views.jobs,
        name="jobs"
    ),

    # Add job
    path(
        "jobs/add/",
        views.add_job,
        name="add_job"
    ),

    # Match resume with jobs
    path(
        "match/<int:resume_id>/",
        views.match_jobs,
        name="match_jobs"
    ),

    # API resume analysis
    path(
        "api/analyze/",
        views.api_analyze,
        name="api_analyze"
    ),
]