# demo_standard_library.py
# The Python Toolbelt: math, os, time, random, datetime

import math
import os
import time
import random
from datetime import datetime, timedelta

print("="*60)
print("     1. MATH MODULE: HIGH-PRECISION NUMERICS              ")
print("="*60)
print(f"PI: {math.pi:.6f}, E: {math.e:.6f}")
print(f"Square Root: {math.sqrt(144)}, Ceiling: {math.ceil(4.2)}, Floor: {math.floor(4.8)}")
print(f"GCD of 48 & 180: {math.gcd(48, 180)}")

print("\n" + "="*60)
print("     2. RANDOM MODULE: SIMULATIONS                        ")
print("="*60)
students = ["Aman", "Rohan", "Neha", "Pooja", "Vikram"]
print("Random Choice (Lucky Draw Winner):", random.choice(students))
random.shuffle(students)
print("Shuffled Lab Seating:", students)
print("Random Roll Number (1-100):", random.randint(1, 100))

print("\n" + "="*60)
print("     3. OS MODULE: DIRECTORY INSPECTION                   ")
print("="*60)
print("Current Working Directory:", os.getcwd())
print("Files in workspace:", os.listdir('.')[:5])

print("\n" + "="*60)
print("     4. DATETIME MODULE: DATE ARITHMETIC                  ")
print("="*60)
now = datetime.now()
print("Current Timestamp:", now.strftime("%Y-%m-%d %H:%M:%S"))
exam_deadline = now + timedelta(days=14, hours=6)
print("Final Exam Deadline:", exam_deadline.strftime("%A, %d %B %Y"))
