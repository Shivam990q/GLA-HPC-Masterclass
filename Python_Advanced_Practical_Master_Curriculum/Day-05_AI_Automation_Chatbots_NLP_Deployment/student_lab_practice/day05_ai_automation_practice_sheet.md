# Day 5: AI Automation Practice Sheet (GLA B.Tech CSE)

## Problem 1: Spam Detection Microservice
- Train a TF-IDF + Multinomial Naive Bayes text classifier on synthetic email messages.
- Wrap the model in a FastAPI endpoint `POST /classify_email` returning `{"is_spam": bool, "confidence": float}`.

## Problem 2: Rule-Based & Keyword Intent Chatbot
- Implement a chatbot router using regex and keyword matching that answers FAQs for GLA University exams, fee schedules, and hostel rules.

## Problem 3: Automated Email Notification Trigger
- Couple the output of an ML model with an automated action: if an email is flagged as phishing/high-risk, automatically trigger a security log alert.
