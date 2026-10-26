# build_complete_python_bcsg0072.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\Python_BCSG0072_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# MASTER README & INSTRUCTOR PLAYBOOK
# ==============================================================================
write_f("README.md", """
# Python Programming: A Practical Approach (Course Code: BCSG0072)
### Official Master 5-Day Block Teaching Curriculum @ GLA University
**Batch**: B4 (1st Semester B.Tech Freshmen)  
**Lead Trainer**: Shivam Gupta | **Co-Trainer**: Mr. Nikhil  
**Organization**: Edulateral Foundation @ GLA University, Mathura  

---

## 🏛️ Course Overview & Pedagogical Mandate
This 5-day block training program is engineered specifically for **1st-Year B.Tech Computer Science freshmen**. The curriculum directly aligns with GLA University's accredited examination syllabus for **`BCSG0072` (Problem Solving with Python)**.

```mermaid
graph TD
    D1["<b>Day 1: Logic, Conditionals, Loops, Lists & Strings</b><br>Basics, 15 List Methods, Slicing, 18 String Methods, Comprehensions"]
    D2["<b>Day 2: Collections, Functions & Functional Programming</b><br>Tuples, Sets, Dictionaries, Scope (LEGB), *args/**kwargs, map/filter/reduce"]
    D3["<b>Day 3: Recursion, Memory Stack & The Standard Library</b><br>Call Stack, sys.setrecursionlimit, Tower of Hanoi, os, math, random, time, numpy"]
    D4["<b>Day 4: Defensive Coding & Persistent File Handling</b><br>Errors vs Exceptions, try-except-else-finally, with open(), Text & CSV data"]
    D5["<b>Day 5: Pattern Matching (Regex) & Shipping Capstone Projects</b><br>re module, Validation, 6 End-to-End Terminal/File-backed Portfolio Projects"]

    D1 --> D2 --> D3 --> D4 --> D5
```

---

## 📅 Daily Curriculum Breakdown

1. **[Day 1: Basics, Control Flow, Lists & Strings](./Day-01_Python_Basics_Lists_Strings/)**:
   - Variables, dynamic typing, `if-elif-else`, ternary operators.
   - `for` & `while` loops, loop `else`, `break`/`continue`/`pass`.
   - 15 List methods, step slicing `[::-1]`, list comprehensions, `enumerate()`, `zip()`.
   - 18 String methods, string formatting (f-strings).

2. **[Day 2: Collections, Functions & Functional Pipelines](./Day-02_Collections_Functions_Functional/)**:
   - Tuples (12 methods), Sets (15 methods & set algebra).
   - Dictionaries (15 methods & comprehensions).
   - Modular functions: positional, keyword, default, `*args`, `**kwargs`.
   - Variable scope: **LEGB Rule** (Local -> Enclosing -> Global -> Built-in), `nonlocal`.
   - Functional programming: `lambda`, `map()`, `filter()`, `functools.reduce()`.

3. **[Day 3: Recursion, Modules & Standard Library](./Day-03_Recursion_Modules_StdLib/)**:
   - Recursion mechanics, call stack frames, stack overflow, `sys.setrecursionlimit`.
   - Classic problems: Factorial, Fibonacci, Palindrome, Binary Search, Tower of Hanoi.
   - Memoization caching (`functools.lru_cache`).
   - Modules & packages: `__name__ == '__main__'`, `__init__.py`.
   - Standard library toolbelt: `math` (12 funcs), `time` (8 funcs), `os` (12 funcs), `random`, `datetime`, intro to `numpy`.

4. **[Day 4: Exception Handling & File I/O](./Day-04_Exceptions_File_Handling/)**:
   - Errors vs Exceptions (`ZeroDivision`, `ValueError`, `KeyError`, `IndexError`, `FileNotFound`).
   - `try`, `except` (multiple & aliased), `else`, `finally`.
   - `raise`, `assert`, custom user-defined exceptions.
   - File handling: `open()`, context manager `with`, modes (`r`, `w`, `a`, `r+`), 10 stream methods.
   - Working with text files and CSV structured tabular data.

5. **[Day 5: Regular Expressions & Capstone Projects](./Day-05_Regex_Projects_Database/)**:
   - Pattern matching with `re`: raw strings, metacharacters, character classes, `search`, `findall`, `sub`, groups.
   - Database connectivity overview (`sqlite3`).
   - **6 Complete Capstone Projects**:
     1. Smart Contact Book (File-backed CRUD)
     2. Student Grade Analyzer (Lists, Dicts, Map/Filter/Reduce)
     3. Quiz Game (Random questions + persistent scoreboard)
     4. Personal Expense Tracker (Categorization & totals)
     5. Email & Log Validator (Regex-driven parsing)
     6. ATM / Library Simulation (Defensive object/function design)

---

## 🏆 Daily Lab & Doubts Policy
As mandated by GLA University:
* Every student must receive **daily practice questions** covering that day's topics.
* Lead and co-trainers must ensure **100% completion in the lab**.
* Active doubt-clearing sessions run after every major topic block.
""")

write_f("INSTRUCTOR_PLAYBOOK.md", """
# 🎙️ Shivam Gupta's Master Instructor Playbook
### The Definitive Guide to Teaching 1st-Year Freshmen (GLA University)

---

## 🧠 Part 1: Freshman Psychology (The Day 1 Mindset)
1. **The Fear Factor**:
   * 60% of first-year students have never written a line of code in their life.
   * They fear getting syntax errors in front of their peers.
   * **Your Golden Rule**: *"Errors are not mistakes; they are Python talking to you."* Celebrate errors on the projector!
2. **The "Copy-Paste" Trap**:
   * If you give them code to copy-paste, they learn zero logic.
   * Make them type every single line. Use live interactive REPL and VS Code live coding.
3. **The Common Pitfalls to Address Immediately**:
   * **IndentationError**: Freshmen mix Tabs and Spaces. Show them VS Code's "Convert Indentation to Spaces" setting.
   * **Print vs Return**: They confuse printing on screen with returning values from functions.
   * **Input is always string**: Remind them that `input()` returns string, requiring `int(input())`.

---

## ⚡ Part 2: Two-Trainer Synergy (Shivam + Nikhil)
* **Shivam (Lead Trainer - Projector & Mic)**:
  - Explains the mental model on the whiteboard (Draw memory boxes, pointers, call stacks).
  - Types the code live on the projector slowly, explaining every keyword.
  - Keeps the class energy high, asks questions to random rows.
* **Nikhil (Floor Support - Lab Aisle Marshall)**:
  - Walks the lab rows constantly.
  - As soon as a student raises a hand, reaches them within 20 seconds.
  - Resolves local PC setup, indentation errors, and keyboard shortcuts without stopping the lecture flow.

---

## 🕒 Part 3: The 9 AM to 5 PM Daily Rhythm
* **09:00 AM - 10:30 AM**: Block 1 — Concept Whiteboard + Live Demonstration.
* **10:30 AM - 10:45 AM**: Short Break.
* **10:45 AM - 01:00 PM**: Block 2 — Deep Dive + Hands-on Lab Milestone 1.
* **01:00 PM - 02:00 PM**: Lunch Break.
* **02:00 PM - 03:30 PM**: Block 3 — Advanced Concept + Live Interactive Coding.
* **03:30 PM - 04:30 PM**: Block 4 — Student Practice Challenge Sheet (Mandatory 100% completion).
* **04:30 PM - 05:00 PM**: Hot Seat Q&A + Day Wrap-up & Tomorrow's Teaser.
""")

print("Master README & Instructor Playbook generated successfully.")
