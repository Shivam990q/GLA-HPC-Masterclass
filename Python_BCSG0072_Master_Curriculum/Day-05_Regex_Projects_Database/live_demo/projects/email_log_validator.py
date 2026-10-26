# email_log_validator.py
# Capstone Project 5: Regex Email & Server Log Parsing Engine
import re

LOG_SAMPLES = [
    "2026-10-05 10:14:02 [ERROR] User login failed for email user.one@domain.com from IP 192.168.1.15",
    "2026-10-05 10:14:05 [INFO] Password reset sent to contact@gla.ac.in",
    "2026-10-05 10:15:30 [ERROR] Malformed packet from invalid_email@domain, dropping connection",
    "2026-10-05 10:16:11 [WARN] Phone number +91-9876543210 triggered rate limit",
    "2026-10-05 10:17:45 [ERROR] Auth timeout for test.student@gmail.com"
]

EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
PHONE_PATTERN = re.compile(r"(?:\+91-)?[6-9]\d{9}")

print("="*65)
print("          REGEX SERVER LOG ANALYZER & SANITIZER          ")
print("="*65)

error_count = 0
found_emails = []

for log in LOG_SAMPLES:
    if "[ERROR]" in log:
        error_count += 1
    emails = EMAIL_PATTERN.findall(log)
    ips = IP_PATTERN.findall(log)
    phones = PHONE_PATTERN.findall(log)
    
    if emails:
        found_emails.extend(emails)
        print(f"[EXTRACTED EMAIL] {emails[0]}")
    if ips:
        print(f"[EXTRACTED IP]    {ips[0]}")
    if phones:
        print(f"[EXTRACTED PHONE] {phones[0]}")

print("-"*65)
print(f"[+] Total Error Events Detected: {error_count}")
print(f"[+] Extracted Unique Verified Emails: {list(set(found_emails))}")
print("="*65)
