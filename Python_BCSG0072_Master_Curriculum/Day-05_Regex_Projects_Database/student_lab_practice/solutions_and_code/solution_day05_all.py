# solution_day05_all.py
# Complete Reference Solutions for ALL 10 Day 5 Lab Practice Problems
import re
import sqlite3

print("="*60)
print("     DAY 5: COMPLETE SOLUTIONS (PROBLEMS 1 TO 10)         ")
print("="*60)

# Problem 1: Email Validator
email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
print("Problem 1 Email 'student.gla@gla.ac.in' Valid:", bool(email_regex.match("student.gla@gla.ac.in")))

# Problem 2: Indian Phone Number Validator
phone_regex = re.compile(r"^(?:\+91-)?[6-9]\d{9}$")
print("Problem 2 Phone '+91-9876543210' Valid:", bool(phone_regex.match("+91-9876543210")))

# Problem 3: URL Extractor
text_urls = "Visit https://www.gla.ac.in or http://portal.glau.in/login for info."
urls = re.findall(r"https?://[\w.-]+(?:/[\w.-]*)*", text_urls)
print("Problem 3 Extracted URLs:", urls)

# Problem 4: Date Extractor
sample_dates = "Exam dates: 12/10/2026 and backup 2026-11-05."
dates = re.findall(r"\b(?:\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\b", sample_dates)
print("Problem 4 Extracted Dates:", dates)

# Problem 5: Words Starting with Vowels
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*", "An elephant is eating orange apples in India")
print("Problem 5 Vowel-Starting Words:", vowel_words)

# Problem 6: HTML Tag Stripper
html_snippet = "<h1>Welcome</h1><p>This is <b>bold</b> text.</p>"
clean_text = re.sub(r"<[^>]+>", "", html_snippet)
print("Problem 6 Stripped Text:", f"'{clean_text}'")

# Problem 7: Credit Card Obfuscator
card_num = "1234-5678-9012-3456"
masked = re.sub(r"\d{4}-\d{4}-\d{4}-(\d{4})", r"****-****-****-\1", card_num)
print("Problem 7 Masked Card:", masked)

# Problem 8: Hashtag & Mention Extractor
tweet = "Loving the #Python workshop at @GLA_University! #Coding #AI"
hashtags = re.findall(r"#\w+", tweet)
mentions = re.findall(r"@\w+", tweet)
print("Problem 8 Hashtags:", hashtags)
print("Problem 8 Mentions:", mentions)

# Problem 9 & 10: SQLite Table Creation, Insertion & Query
conn = sqlite3.connect(":memory:") # In-memory database for testing
cursor = conn.cursor()
cursor.execute("CREATE TABLE students (id INT PRIMARY KEY, name TEXT, score INT)")
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", [
    (101, "Aarav", 88),
    (102, "Neha", 96),
    (103, "Rohan", 74)
])
conn.commit()

cursor.execute("SELECT name, score FROM students ORDER BY score DESC LIMIT 1")
topper = cursor.fetchone()
print(f"Problem 10 SQLite Query Topper: {topper[0]} with Score {topper[1]}")
conn.close()
print("="*60)
