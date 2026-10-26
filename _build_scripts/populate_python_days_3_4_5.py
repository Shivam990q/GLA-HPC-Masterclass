# populate_python_days_3_4_5.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\Python_BCSG0072_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 3: RECURSION, MODULES & STANDARD LIBRARY
# ==============================================================================
write_f("Day-03_Recursion_Modules_StdLib/theory_notes/day03_theory_guide.md", """
# Day 3: Recursion, Call Stack Mechanics, Modules & The Standard Library

---

### 1. Recursion First Principles
- **Definition**: A function calling itself directly or indirectly to solve smaller instances of the same problem.
- **The Two Mandatory Components**:
  1. **Base Case**: The termination condition that returns a value without making further recursive calls.
  2. **Recursive Step**: Calling the function with an altered argument that moves closer to the base case.
- **The Call Stack Under the Hood**:
  - Each recursive call pushes a new **Stack Frame** (activation record) containing local variables and return address onto the call stack.
  - When base case is met, stack frames begin **unwinding** (popping) and returning values.
  - **Stack Overflow**: Exceeding the maximum recursion depth. Inspect with `sys.getrecursionlimit()` and set with `sys.setrecursionlimit()`.
- **Recursion vs Iteration**:
  - Iteration uses fixed memory; recursion uses $O(N)$ stack memory.
  - Tree-like structures (DOM, File systems, JSON, ASTs) are naturally recursive.

---

### 2. Classic Recursive Problems
- Factorial: $F(N) = N \\times F(N-1)$
- Fibonacci: $Fib(N) = Fib(N-1) + Fib(N-2)$ ($O(2^N)$ naive vs $O(N)$ memoized).
- Binary Search: Divide and conquer in $O(\\log N)$.
- Tower of Hanoi: Recurrence relation $T(N) = 2T(N-1) + 1 \\to 2^N - 1$ steps.
- **Memoization**:
  - Manual caching using dictionary.
  - Standard library: `@functools.lru_cache(maxsize=None)`.

---

### 3. Modules & Package Architecture
- Creating `.py` modules and import styles:
  `import math`, `from math import sqrt, pi`, `import numpy as np`.
- The `__name__ == '__main__'` idiom: Prevents script execution when imported as a library.
- Packages: Hierarchical directories containing an `__init__.py` file.

---

### 4. The Python Standard Library Toolbelt
- **`math` (12 Core Functions)**:
  `sqrt()`, `pow()`, `ceil()`, `floor()`, `factorial()`, `gcd()`, `fabs()`, `log()`, `sin()`, `cos()`, `pi`, `e`.
- **`time` (8 Core Functions)**:
  `time()`, `sleep()`, `ctime()`, `localtime()`, `gmtime()`, `strftime()`, `mktime()`, `perf_counter()`.
- **`os` (12 Core Functions)**:
  `getcwd()`, `listdir()`, `mkdir()`, `makedirs()`, `rmdir()`, `remove()`, `rename()`, `path.exists()`, `path.join()`, `path.isfile()`, `path.isdir()`, `path.getsize()`.
- **`random`**:
  `random()`, `randint(a, b)`, `choice(seq)`, `shuffle(list)`, `sample(seq, k)`, `seed(val)`.
- **`datetime`**:
  `date.today()`, `datetime.now()`, `timedelta` date arithmetic.
- **Introduction to `numpy`**:
  Vectorized arrays, `np.arange()`, `np.reshape()`, `np.mean()`, `np.sum()`.
""")

write_f("Day-03_Recursion_Modules_StdLib/live_demo/demo_recursion_visualizer.py", """
# demo_recursion_visualizer.py
# Recursion call stack demonstration and memoization benchmark
import time
from functools import lru_cache

print("="*60)
print("     DEMO 1: VISUALIZING RECURSIVE CALL STACK             ")
print("="*60)

def visual_factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}-> factorial({n}) called (Stack Frame {depth})")
    if n <= 1:
        print(f"{indent}<- Base Case reached: returning 1")
        return 1
    result = n * visual_factorial(n - 1, depth + 1)
    print(f"{indent}<- Unwinding: returning {n} * fact({n-1}) = {result}")
    return result

visual_factorial(4)

print("\\n" + "="*60)
print("     DEMO 2: TOWER OF HANOI (3 DISKS)                     ")
print("="*60)

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'Pole A', 'Pole C', 'Pole B')

print("\\n" + "="*60)
print("     DEMO 3: MEMOIZATION WITH LRU_CACHE (FIBONACCI)       ")
print("="*60)

@lru_cache(maxsize=None)
def memo_fib(n):
    if n < 2:
        return n
    return memo_fib(n - 1) + memo_fib(n - 2)

t0 = time.perf_counter()
fib_val = memo_fib(100)
elapsed = time.perf_counter() - t0
print(f"Fibonacci(100) computed in {elapsed:.6f}s via @lru_cache:")
print(f"Result: {fib_val}")
""")

write_f("Day-03_Recursion_Modules_StdLib/live_demo/demo_standard_library.py", """
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

print("\\n" + "="*60)
print("     2. RANDOM MODULE: SIMULATIONS                        ")
print("="*60)
students = ["Aman", "Rohan", "Neha", "Pooja", "Vikram"]
print("Random Choice (Lucky Draw Winner):", random.choice(students))
random.shuffle(students)
print("Shuffled Lab Seating:", students)
print("Random Roll Number (1-100):", random.randint(1, 100))

print("\\n" + "="*60)
print("     3. OS MODULE: DIRECTORY INSPECTION                   ")
print("="*60)
print("Current Working Directory:", os.getcwd())
print("Files in workspace:", os.listdir('.')[:5])

print("\\n" + "="*60)
print("     4. DATETIME MODULE: DATE ARITHMETIC                  ")
print("="*60)
now = datetime.now()
print("Current Timestamp:", now.strftime("%Y-%m-%d %H:%M:%S"))
exam_deadline = now + timedelta(days=14, hours=6)
print("Final Exam Deadline:", exam_deadline.strftime("%A, %d %B %Y"))
""")

# ==============================================================================
# DAY 4: EXCEPTIONS & FILE HANDLING
# ==============================================================================
write_f("Day-04_Exceptions_File_Handling/theory_notes/day04_theory_guide.md", """
# Day 4: Defensive Coding, Exception Architecture & Persistent File I/O

---

### 1. Errors vs Exceptions
- **Syntax Errors**: Parsing stage failures (invalid indentation, missing colons). Program does not start.
- **Runtime Exceptions**: Logical failures during execution. Unhandled exceptions crash the program with a traceback.
- **Common Standard Exceptions**:
  `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, `AttributeError`.

---

### 2. The Complete Exception Handling Block
```python
try:
    # Risky code
    value = 10 / divisor
except ZeroDivisionError as e:
    # Catches specific error
    print("Cannot divide by zero")
except (ValueError, TypeError) as e:
    # Catches multiple errors
    print("Invalid data type or value")
else:
    # Executes ONLY if NO exception was raised in try block
    print("Success! Result is:", value)
finally:
    # GUARANTEED to execute (ideal for closing files / db connections)
    print("Cleanup complete.")
```

- **Raising Exceptions**: `raise ValueError("Age must be >= 18")`
- **Assertions**: `assert condition, "Error message"`
- **Custom User-Defined Exceptions**:
  ```python
  class InsufficientFundsError(Exception):
      \"\"\"Raised when account balance is lower than withdrawal amount.\"\"\"
      pass
  ```

---

### 3. File Handling Mechanics
- File Streams and Context Managers:
  ```python
  with open("data.txt", "w", encoding="utf-8") as file:
      file.write("Hello World")
  # File automatically closed, even if an exception occurs inside!
  ```
- **File Modes**:
  `'r'` (Read), `'w'` (Write/Overwrite), `'a'` (Append), `'r+'` (Read/Write), `'rb'` / `'wb'` (Binary modes).
- **The 10 Core Stream Methods**:
  1. `read([size])`: Reads entire content or specified bytes.
  2. `readline()`: Reads single line including `\\n`.
  3. `readlines()`: Reads all lines into a list of strings.
  4. `write(str)`: Writes string to stream.
  5. `writelines(list)`: Writes sequence of strings.
  6. `seek(offset, whence)`: Moves file pointer to byte position.
  7. `tell()`: Returns current byte offset of file pointer.
  8. `flush()`: Forces buffer flush to physical disk.
  9. `close()`: Closes stream and releases OS file handle.
  10. `truncate([size])`: Truncates file to specified byte size.
""")

write_f("Day-04_Exceptions_File_Handling/live_demo/demo_file_handling.py", """
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
    f.write("26001,Aarav,88\\n")
    f.write("26002,Neha,95\\n")
    f.write("26003,Rohan,64\\n")
    f.write("26004,Pooja,79\\n")
print(f"[+] Successfully wrote records to {FILENAME}")

# Reading back line-by-line
print("\\nReading line by line with .readline():")
with open(FILENAME, "r", encoding="utf-8") as f:
    for line in f:
        roll, name, score = line.strip().split(",")
        print(f"  Roll: {roll} | Name: {name:<8} | Score: {score}")

print("\\n" + "="*60)
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
""")

# ==============================================================================
# DAY 5: REGEX & ALL 6 CAPSTONE PROJECTS!
# ==============================================================================
write_f("Day-05_Regex_Projects_Database/theory_notes/day05_theory_guide.md", """
# Day 5: Regular Expressions (`re`), Database Connectivity & Capstone Engineering

---

### 1. Regular Expressions First Principles
- A Domain-Specific Language (DSL) for string pattern matching and validation.
- The `re` module and raw strings `r\"...\"` (prevents backslash escaping).
- **Core Metacharacters**:
  - `.` : Any single character except newline.
  - `^` : Start of string / line anchor.
  - `$` : End of string / line anchor.
  - `*` : 0 or more occurrences (greedy).
  - `+` : 1 or more occurrences (greedy).
  - `?` : 0 or 1 occurrence (optional).
  - `[abc]` : Character set (matches 'a', 'b', or 'c').
  - `[^abc]` : Negated set.
  - `{m, n}` : Quantifier range (between $m$ and $n$ times).
  - `|` : Alternation (OR).
- **Character Classes**:
  `\\d` (digits `[0-9]`), `\\D` (non-digits), `\\w` (alphanumeric `[a-zA-Z0-9_]`), `\\s` (whitespace).
- **Core Functions**:
  - `re.search(pattern, str)`: Scans entire string for first match.
  - `re.match(pattern, str)`: Matches ONLY at beginning of string.
  - `re.findall(pattern, str)`: Returns list of all matching substrings.
  - `re.finditer(pattern, str)`: Returns iterator of Match objects.
  - `re.sub(pattern, repl, str)`: Find and replace matches.
  - `re.compile(pattern)`: Compiles regex into reusable RegexObject for high throughput.

---

### 2. Database Connectivity Overview (`sqlite3`)
- Relational databases store structured records in tables with ACID guarantees.
- Python includes zero-configuration embedded database: `import sqlite3`.
- Basic workflow:
  `conn = sqlite3.connect("app.db")` -> `cursor = conn.cursor()` -> `cursor.execute("CREATE TABLE...")` -> `conn.commit()` -> `conn.close()`.
""")

# PROJECT 1: Contact Book
write_f("Day-05_Regex_Projects_Database/live_demo/projects/contact_book.py", """
# contact_book.py
# Capstone Project 1: Smart Contact Book with Persistent File Storage
import os
import re

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        for c in contacts.values():
            f.write(f"{c['name']}|{c['phone']}|{c['email']}\\n")

def add_contact(contacts):
    name = input("Enter Contact Name: ").strip()
    phone = input("Enter 10-digit Phone: ").strip()
    if not re.match(r"^[6-9]\\d{9}$", phone):
        print("[!] Invalid Indian phone number format!")
        return
    email = input("Enter Email Address: ").strip()
    if not re.match(r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$", email):
        print("[!] Invalid email format!")
        return
    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
    print(f"[+] Contact '{name}' saved successfully!")

def search_contact(contacts):
    query = input("Search by Name: ").strip().lower()
    match = contacts.get(query)
    if match:
        print(f"\\nFound: {match['name']} | Phone: {match['phone']} | Email: {match['email']}")
    else:
        print("[-] Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\\n=== SMART CONTACT BOOK ===")
        print("1. Add Contact\\n2. Search Contact\\n3. View All\\n4. Exit")
        choice = input("Enter Choice (1-4): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            print("\\n--- All Contacts ---")
            for c in contacts.values():
                print(f"Name: {c['name']:<15} | Phone: {c['phone']} | Email: {c['email']}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
""")

# PROJECT 2: Student Grade Analyzer
write_f("Day-05_Regex_Projects_Database/live_demo/projects/student_grade_analyzer.py", """
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
""")

# PROJECT 3: Quiz Game
write_f("Day-05_Regex_Projects_Database/live_demo/projects/quiz_game.py", """
# quiz_game.py
# Capstone Project 3: Interactive Python Quiz Game with Persistent Score History
import random
import os
import time

SCORE_FILE = "quiz_scores.txt"

QUESTIONS = [
    {"q": "What is the output of print(type([]))?", "opts": ["A) list", "B) tuple", "C) dict", "D) set"], "ans": "A"},
    {"q": "Which keyword creates an anonymous function?", "opts": ["A) def", "B) anon", "C) lambda", "D) func"], "ans": "C"},
    {"q": "Which data structure is immutable in Python?", "opts": ["A) list", "B) set", "C) tuple", "D) dict"], "ans": "C"},
    {"q": "What does range(5) produce?", "opts": ["A) 1 to 5", "B) 0 to 4", "C) 0 to 5", "D) 1 to 4"], "ans": "B"},
    {"q": "What is the time complexity of dictionary key lookup?", "opts": ["A) O(N)", "B) O(log N)", "C) O(1)", "D) O(N^2)"], "ans": "C"}
]

def play_quiz():
    name = input("Enter Player Name: ").strip()
    score = 0
    shuffled_q = random.sample(QUESTIONS, len(QUESTIONS))
    
    print(f"\\nWelcome {name}! Answer 5 questions. Type A, B, C, or D.")
    t0 = time.time()
    
    for i, item in enumerate(shuffled_q, 1):
        print(f"\\nQ{i}: {item['q']}")
        for opt in item['opts']:
            print(f"   {opt}")
        ans = input("Your answer: ").strip().upper()
        if ans == item['ans']:
            print("[+] Correct!")
            score += 1
        else:
            print(f"[-] Wrong! Correct answer was: {item['ans']}")
            
    elapsed = time.time() - t0
    print(f"\\nQuiz Finished! Score: {score}/{len(QUESTIONS)} in {elapsed:.1f} seconds")
    
    # Save score history
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name}|{score}/{len(QUESTIONS)}|{elapsed:.1f}s|{time.strftime('%Y-%m-%d %H:%M')}\\n")
    print(f"[+] Score saved to {SCORE_FILE}")

if __name__ == "__main__":
    play_quiz()
""")

# PROJECT 4: Expense Tracker
write_f("Day-05_Regex_Projects_Database/live_demo/projects/expense_tracker.py", """
# expense_tracker.py
# Capstone Project 4: Personal Expense Tracker with Categorization & File Persistence
import os

EXPENSE_FILE = "expenses.txt"

def add_expense():
    category = input("Enter Category (Food/Travel/Study/Fun): ").strip().capitalize()
    try:
        amount = float(input("Enter Amount (INR): "))
    except ValueError:
        print("[!] Please enter a valid number!")
        return
    desc = input("Brief Description: ").strip()
    with open(EXPENSE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{category}|{amount:.2f}|{desc}\\n")
    print("[+] Expense recorded successfully!")

def view_summary():
    if not os.path.exists(EXPENSE_FILE):
        print("[-] No expenses recorded yet.")
        return
    categories = {}
    total = 0.0
    with open(EXPENSE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                cat, amt, desc = parts[0], float(parts[1]), parts[2]
                categories[cat] = categories.get(cat, 0.0) + amt
                total += amt
    print("\\n=== EXPENSE SUMMARY BY CATEGORY ===")
    for cat, amt in categories.items():
        percentage = (amt / total) * 100
        print(f"  {cat:<10}: Rs. {amt:>8.2f}  ({percentage:>5.1f}%)")
    print("-" * 35)
    print(f"  TOTAL     : Rs. {total:>8.2f}")

def main():
    while True:
        print("\\n--- PERSONAL EXPENSE TRACKER ---")
        print("1. Add Expense\\n2. View Summary\\n3. Exit")
        c = input("Choice: ").strip()
        if c == "1": add_expense()
        elif c == "2": view_summary()
        elif c == "3": break
        else: print("[!] Invalid choice")

if __name__ == "__main__":
    main()
""")

# PROJECT 5: Email and Log Validator
write_f("Day-05_Regex_Projects_Database/live_demo/projects/email_log_validator.py", """
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

EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}")
IP_PATTERN = re.compile(r"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b")
PHONE_PATTERN = re.compile(r"(?:\\+91-)?[6-9]\\d{9}")

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
""")

# PROJECT 6: ATM Simulation
write_f("Day-05_Regex_Projects_Database/live_demo/projects/atm_simulation.py", """
# atm_simulation.py
# Capstone Project 6: ATM Banking Simulation using Functions & Custom Exceptions

class InsufficientBalanceError(Exception):
    \"\"\"Raised when withdrawal exceeds available balance.\"\"\"
    pass

class InvalidPINError(Exception):
    \"\"\"Raised when wrong PIN is entered.\"\"\"
    pass

accounts = {
    "1001": {"name": "Aarav Sharma", "pin": "1234", "balance": 15000.0}
}

def verify_pin(acc_num, entered_pin):
    acc = accounts.get(acc_num)
    if not acc or acc["pin"] != entered_pin:
        raise InvalidPINError("Incorrect Account Number or PIN!")
    return acc

def withdraw(acc, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive!")
    if amount > acc["balance"]:
        raise InsufficientBalanceError(f"Insufficient funds! Available balance: Rs. {acc['balance']:.2f}")
    acc["balance"] -= amount
    print(f"[+] Please collect Rs. {amount:.2f}. Remaining Balance: Rs. {acc['balance']:.2f}")

def deposit(acc, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive!")
    acc["balance"] += amount
    print(f"[+] Deposited Rs. {amount:.2f}. New Balance: Rs. {acc['balance']:.2f}")

def main():
    print("=== SECURE ATM BANKING SIMULATION ===")
    acc_no = input("Enter Account Number: ").strip()
    pin = input("Enter 4-digit PIN: ").strip()
    
    try:
        current_acc = verify_pin(acc_no, pin)
        print(f"\\nWelcome {current_acc['name']}!")
        while True:
            print("\\n1. Check Balance\\n2. Withdraw Cash\\n3. Deposit Cash\\n4. Exit")
            ch = input("Select: ").strip()
            if ch == "1":
                print(f"[i] Balance: Rs. {current_acc['balance']:.2f}")
            elif ch == "2":
                amt = float(input("Amount to withdraw: "))
                withdraw(current_acc, amt)
            elif ch == "3":
                amt = float(input("Amount to deposit: "))
                deposit(current_acc, amt)
            elif ch == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("[!] Invalid option")
    except (InvalidPINError, InsufficientBalanceError, ValueError) as e:
        print(f"[ERROR] Transaction Failed: {e}")

if __name__ == "__main__":
    main()
""")

print("Days 3, 4, 5 and ALL 6 PROJECTS generated successfully!")
