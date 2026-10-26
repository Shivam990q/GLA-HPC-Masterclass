# demo_dictionaries.py
# Complete live demonstration of Dictionaries, Comprehensions, and LEGB Scope

print("="*60)
print("      DICTIONARY METHODS & SAFE RETRIEVAL                ")
print("="*60)

student = {
    "name": "Aarav Sharma",
    "roll": "260012",
    "branch": "CSE",
    "cgpa": 8.75
}

# Safe access with .get() (never crashes)
phone = student.get("phone", "Not Provided")
print(f"Student: {student['name']} | Phone: {phone}")

# Iterating keys, values, items
print("\nStudent Record:")
for key, val in student.items():
    print(f"  {key.upper()}: {val}")

# Dictionary Comprehension: Grade categorization
marks = {"Aarav": 88, "Neha": 92, "Rohan": 64, "Priya": 79}
grades = {name: ("A" if m >= 90 else "B" if m >= 75 else "C") for name, m in marks.items()}
print("\nGenerated Grades via Dict Comprehension:")
print(grades)

print("\n" + "="*60)
print("      FUNCTION *ARGS, **KWARGS & LEGB SCOPE               ")
print("="*60)

def university_enrollment(course, *students, **metadata):
    """Demonstrating variable arguments and kwargs."""
    print(f"Course: {course}")
    print(f"Enrolled Students ({len(students)}): {', '.join(students)}")
    print("Metadata:", metadata)

university_enrollment("BCSG0072", "Amit", "Pooja", "Rahul", semester="1st", lab="Lab 4")
