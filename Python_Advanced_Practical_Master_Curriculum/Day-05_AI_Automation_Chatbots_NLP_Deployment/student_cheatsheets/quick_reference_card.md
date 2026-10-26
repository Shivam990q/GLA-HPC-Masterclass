# Day 5 Cheatsheet: AI Automation & NLP Quick Reference

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
query_vec = vectorizer.transform([user_query])

similarity_scores = cosine_similarity(query_vec, X)
best_match_idx = similarity_scores.argmax()
```
