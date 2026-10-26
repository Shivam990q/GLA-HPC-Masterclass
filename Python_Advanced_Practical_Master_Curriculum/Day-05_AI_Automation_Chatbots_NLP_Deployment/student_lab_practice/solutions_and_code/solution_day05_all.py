# solution_day05_all.py
# Working solutions for Day 5 AI Automation practice problems

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Synthetic Training Data for Spam Filter
corpus = [
    "Win a free iPhone now click here",
    "Claim your lottery prize of 1 million dollars",
    "URGENT: Your bank account is locked verify immediately",
    "Dear student, your GLA semester exam schedule is attached",
    "Meeting rescheduled to 3 PM tomorrow in Conference Hall",
    "Please review the attached project assignment before Friday",
]
labels = [1, 1, 1, 0, 0, 0] # 1 = Spam, 0 = Ham

spam_pipe = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])
spam_pipe.fit(corpus, labels)

app = FastAPI(title="Spam Detection Service")

class EmailRequest(BaseModel):
    subject: str
    body: str

@app.post("/classify_email")
def classify(req: EmailRequest):
    text = f"{req.subject} {req.body}"
    pred = spam_pipe.predict([text])[0]
    prob = spam_pipe.predict_proba([text])[0][pred]
    return {
        "classification": "SPAM" if pred == 1 else "LEGITIMATE (HAM)",
        "confidence": round(float(prob), 4)
    }

if __name__ == "__main__":
    print("[*] Running Spam Detection AI Service on port 8002...")
    uvicorn.run(app, host="127.0.0.1", port=8002)
