# student_grade_analyzer.py
# Capstone Project 2: Student Grade Analyzer using Functional Pipelines (map/filter/reduce)
from functools import reduce

students = [
    {"roll": 101, "name": "Aarav", "marks": [85, 90, 88, 92]},
    {"roll": 102, "name": "Neha", "marks": [95, 96, 92, 98]},
    {"roll": 103, "name": "Rohan", "marks": [60, 55, 65, 70]},
    {"roll": 104, "name": "Priya", "marks": [78, 82, 80, 85]}
]

# Calculate averages using map and lambda
records = list(map(lambda s: {
    "roll": s["roll"],
    "name": s["name"],
    "average": sum(s["marks"]) / len(s["marks"]),
    "grade": "A+" if sum(s["marks"])/len(s["marks"]) >= 90 else "A" if sum(s["marks"])/len(s["marks"]) >= 75 else "B"
}, students))

# Identify Class Topper using reduce
topper = reduce(lambda s1, s2: s1 if s1["average"] > s2["average"] else s2, records)

# Filter Distinction Students (Average >= 75)
distinction_students = list(filter(lambda s: s["average"] >= 75, records))

print("="*60)
print("             STUDENT GRADE ANALYTICS REPORT               ")
print("="*60)
for r in records:
    print(f"Roll: {r['roll']} | Name: {r['name']:<8} | Avg: {r['average']:.2f}% | Grade: {r['grade']}")
print("-"*60)
print(f"[🏆] Class Topper: {topper['name']} with {topper['average']:.2f}%")
print(f"[+] Total Distinction Holders: {len(distinction_students)} / {len(students)}")
print("="*60)
