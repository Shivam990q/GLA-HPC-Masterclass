# demo_file_handling.py
# Complete live demonstration of Safe File Handling & CSV Data Processing

import os
import csv

FILENAME = "students_database.txt"
CSV_FILENAME = "marks_report.csv"

print("="*60)
print("     DEMO 1: CONTEXT MANAGERS & WRITING PERSISTENT DATA   ")
print("="*60)

# Writing structured lines
with open(FILENAME, "w", encoding="utf-8") as f:
    f.write("26001,Aarav,88\n")
    f.write("26002,Neha,95\n")
    f.write("26003,Rohan,64\n")
    f.write("26004,Pooja,79\n")
print(f"[+] Successfully wrote records to {FILENAME}")

# Reading back line-by-line
print("\nReading line by line with .readline():")
with open(FILENAME, "r", encoding="utf-8") as f:
    for line in f:
        roll, name, score = line.strip().split(",")
        print(f"  Roll: {roll} | Name: {name:<8} | Score: {score}")

print("\n" + "="*60)
print("     DEMO 2: CSV TABULAR EXPORT & ANALYSIS               ")
print("="*60)

data = [
    ["Roll", "Name", "Subject", "Marks"],
    ["101", "Aarav", "Python", 92],
    ["102", "Neha", "Python", 98],
    ["103", "Rohan", "Python", 72]
]

with open(CSV_FILENAME, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)
print(f"[+] Generated CSV File: {CSV_FILENAME}")

# Read and calculate class average
total_marks = 0
count = 0
with open(CSV_FILENAME, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_marks += int(row["Marks"])
        count += 1
print(f"[+] Calculated Class Average: {total_marks / count:.2f} marks")
