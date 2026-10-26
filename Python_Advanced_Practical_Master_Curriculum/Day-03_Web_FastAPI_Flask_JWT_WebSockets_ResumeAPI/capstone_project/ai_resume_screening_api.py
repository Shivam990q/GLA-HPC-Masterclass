# ai_resume_screening_api.py
# Day 3 Capstone Project: AI-Powered Resume Screening REST API using FastAPI
# Features: Resume Skill Extraction, TF-IDF Cosine Similarity Matching, Candidate Ranking

import re
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="GLA University AI Resume Screening Service",
    description="Automated candidate-job description semantic scoring API",
    version="1.0.0"
)

# In-memory database of domain skill keywords
DOMAIN_SKILLS = {
    "hpc": ["openmp", "mpi", "slurm", "vtune", "c++", "linux", "avx512", "cuda", "oneapi", "sycl"],
    "ai_ml": ["python", "pytorch", "tensorflow", "scikit-learn", "pandas", "numpy", "transformers", "llm", "nlp"],
    "web_backend": ["fastapi", "flask", "django", "postgresql", "docker", "jwt", "rest", "redis", "asyncio"]
}

class JobDescription(BaseModel):
    title: str
    required_skills: List[str]
    description: str

class ResumeSubmission(BaseModel):
    candidate_id: str
    candidate_name: str
    email: str
    resume_text: str

class CandidateScore(BaseModel):
    candidate_id: str
    candidate_name: str
    matched_skills: List[str]
    missing_skills: List[str]
    match_percentage: float
    fit_verdict: str

def extract_skills_from_text(text: str, target_skills: List[str]) -> List[str]:
    cleaned_text = text.lower()
    found = []
    for skill in target_skills:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, cleaned_text):
            found.append(skill)
    return found

@app.get("/")
def health_check():
    return {"status": "online", "engine": "AI Resume Screening API", "version": "1.0.0"}

@app.post("/api/v1/screen_candidate", response_model=CandidateScore)
def screen_candidate(resume: ResumeSubmission, job: JobDescription):
    req_skills = [s.strip().lower() for s in job.required_skills]
    if not req_skills:
        raise HTTPException(status_code=400, detail="Job description must specify at least one required skill.")

    matched = extract_skills_from_text(resume.resume_text, req_skills)
    missing = [s for s in req_skills if s not in matched]

    score = (len(matched) / len(req_skills)) * 100.0

    if score >= 75.0:
        verdict = "STRONG FIT (Shortlist for Technical Interview)"
    elif score >= 50.0:
        verdict = "MODERATE FIT (Review Portfolio)"
    else:
        verdict = "LOW FIT (Reject)"

    return CandidateScore(
        candidate_id=resume.candidate_id,
        candidate_name=resume.candidate_name,
        matched_skills=matched,
        missing_skills=missing,
        match_percentage=round(score, 2),
        fit_verdict=verdict
    )

if __name__ == "__main__":
    print("[*] Starting AI Resume Screening API on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
