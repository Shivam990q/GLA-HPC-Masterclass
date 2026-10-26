# ai_customer_support_chatbot.py
# Day 5 Capstone Project: AI-Powered Customer Support Chatbot using NLP Intent Classification & FastAPI
# Features: Intent Matching, Cosine Similarity Scoring, Automated Responses, Session Tracking

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn

app = FastAPI(
    title="GLA University AI Customer Support Bot",
    description="Automated NLP Customer Support Chatbot Service",
    version="1.0.0"
)

# Knowledge Base of Support Intents
KNOWLEDGE_BASE = [
    {
        "intent": "admission_inquiry",
        "patterns": [
            "How do I apply for B.Tech admission at GLA?",
            "What is the eligibility criteria for computer science?",
            "When do admissions open?",
            "Can I get direct admission in GLA university?",
            "What is the fee structure for engineering?"
        ],
        "response": "GLA University admissions for B.Tech CSE require minimum 60% in PCM. Applications are accepted via gla.ac.in/admission with GLAET entrance exam."
    },
    {
        "intent": "hostel_inquiry",
        "patterns": [
            "How are the hostel facilities?",
            "Is hostel mandatory for first year students?",
            "What are the hostel fees and mess food?",
            "Are AC rooms available in the campus hostel?"
        ],
        "response": "GLA University provides on-campus separate hostels for boys and girls with 24/7 Wi-Fi, gym, medical center, and vegetarian mess facilities."
    },
    {
        "intent": "placement_statistics",
        "patterns": [
            "What is the highest package in placements?",
            "Which companies visit for campus placement?",
            "What is the average package for computer engineering?",
            "How are placement records at GLA?"
        ],
        "response": "GLA University boasts a 90%+ placement record. Highest package reached 55 LPA, with an average of 6.5 to 8 LPA across top recruiters including Amazon, TCS, and Capgemini."
    },
    {
        "intent": "hpc_lab_inquiry",
        "patterns": [
            "Where is the High Performance Computing lab located?",
            "Does GLA have an Intel or supercomputing center?",
            "What hardware exists in the HPC lab?",
            "Can students use the Intel oneAPI cluster?"
        ],
        "response": "The Intel Unnati & HPC Center of Excellence is located in the Department of Computer Engineering & Applications, featuring Intel Xeon multicore nodes and oneAPI development suites."
    }
]

# Flatten patterns for vectorization
all_patterns = []
pattern_to_intent = []

for item in KNOWLEDGE_BASE:
    for pat in item["patterns"]:
        all_patterns.append(pat)
        pattern_to_intent.append(item)

vectorizer = TfidfVectorizer(stop_words='english')
pattern_matrix = vectorizer.fit_transform(all_patterns)

class UserQuery(BaseModel):
    session_id: str
    user_message: str

class BotResponse(BaseModel):
    session_id: str
    intent: str
    confidence_score: float
    bot_reply: str

@app.post("/api/v1/chat", response_model=BotResponse)
def handle_chat_message(query: UserQuery):
    msg = query.user_message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="User message cannot be empty.")

    query_vec = vectorizer.transform([msg])
    similarities = cosine_similarity(query_vec, pattern_matrix).flatten()

    best_idx = int(np.argmax(similarities))
    best_score = float(similarities[best_idx])

    # Confidence Thresholding
    if best_score < 0.25:
        return BotResponse(
            session_id=query.session_id,
            intent="unknown_fallback",
            confidence_score=round(best_score, 4),
            bot_reply="I am sorry, I did not quite understand that. Please reach out directly to the GLA helpdesk at support@gla.ac.in."
        )

    matched_item = pattern_to_intent[best_idx]
    return BotResponse(
        session_id=query.session_id,
        intent=matched_item["intent"],
        confidence_score=round(best_score, 4),
        bot_reply=matched_item["response"]
    )

if __name__ == "__main__":
    print("[*] Starting AI Customer Support Chatbot on http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001)
