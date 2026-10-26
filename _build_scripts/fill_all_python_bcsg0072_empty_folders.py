# fill_all_python_bcsg0072_empty_folders.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\Python_BCSG0072_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 2
# ==============================================================================
write_f("Day-02_Collections_Functions_Functional/interview_and_exam_qa/day02_exam_and_interview_qa.md", """
# Day 2: Exam & Interview Q&A (BCSG0072)

### Q1: What is the LEGB rule of variable scope in Python? (5 Marks)
* **Answer**: LEGB defines the order in which Python searches namespaces for a variable:
  1. **L**ocal: Inside current function.
  2. **E**nclosing: In any enclosing nested function scopes (closures).
  3. **G**lobal: At module top-level.
  4. **B**uilt-in: In Python's built-in namespace (`len`, `range`, `print`).

### Q2: What is the difference between `*args` and `**kwargs`? (3 Marks)
* **Answer**: `*args` allows passing a variable number of positional arguments, which Python packs into a `tuple`. `**kwargs` allows passing a variable number of keyword/named arguments, which Python packs into a `dictionary`.

### Q3: Why are dictionary keys required to be immutable? (3 Marks)
* **Answer**: Dictionaries are implemented using Hash Tables. To look up a key in $O(1)$ time, Python computes `hash(key)`. If a key were mutable, modifying its contents would change its hash value, making it impossible to locate in the internal hash table bucket.
""")

write_f("Day-02_Collections_Functions_Functional/presentation_scripts/trainer_speaking_script.md", """
# Day 2 Speaking Script: Shivam Gupta

### ⏰ 09:00 AM - 09:20 AM: Opening Collections
* **Action**: Draw a Dictionary on the board: `student = {"name": "Aarav", "marks": 92}`.
* **Say**:
  > *"Yesterday, we learned lists. In lists, data is stored by index: `list[0]`, `list[1]`. But in real life, data doesn't have index numbers—it has names!*
  > 
  > *Today, we master Dictionaries (Hash Maps) and Sets. In a set of 100,000 students, checking `if roll in student_set` takes $O(1)$ instantaneous time! Then we will learn how functions make our code modular with `*args` and `**kwargs`. Let's code!"*
""")

write_f("Day-02_Collections_Functions_Functional/student_cheatsheets/quick_reference_card.md", """
# Day 2 Quick Reference Card: Collections & Functions

### 1. Dictionary & Set Quick Syntax
* `dict.get(k, default)` / `dict.keys()` / `dict.values()` / `dict.items()`
* Dict Comprehension: `{k: v for k, v in pairs if condition}`
* Set Algebra: `s1 | s2` (Union), `s1 & s2` (Intersection), `s1 - s2` (Difference)

### 2. Functional Tools
* `lambda x, y: x + y`
* `map(func, iterable)`
* `filter(predicate, iterable)`
* `from functools import reduce; reduce(lambda a, b: a * b, [1, 2, 3, 4])`
""")

# ==============================================================================
# DAY 3
# ==============================================================================
write_f("Day-03_Recursion_Modules_StdLib/interview_and_exam_qa/day03_exam_and_interview_qa.md", """
# Day 3: Exam & Interview Q&A (BCSG0072)

### Q1: What causes a Stack Overflow in recursion, and how does Python protect against it? (5 Marks)
* **Answer**: Each recursive call adds a stack frame to the system call stack. If the base case is missing or unreachable, infinite recursive calls consume all allocated stack memory, leading to stack overflow. Python protects against this via a recursion limit (default 1000), raising a `RecursionError` when exceeded.

### Q2: What is the significance of `if __name__ == '__main__':` in Python modules? (3 Marks)
* **Answer**: `__name__` is a built-in variable. When a script is executed directly, `__name__` is set to `'__main__'`. When the script is imported as a module into another file, `__name__` is set to the module's filename. This construct ensures that executable demonstration code runs only when the file is run directly, not when imported.
""")

write_f("Day-03_Recursion_Modules_StdLib/presentation_scripts/trainer_speaking_script.md", """
# Day 3 Speaking Script: Shivam Gupta

### ⏰ 09:00 AM - 09:20 AM: The Call Stack Mental Model
* **Action**: Draw a stack of plates on the whiteboard.
* **Say**:
  > *"Recursion is not magic; it's a stack of plates. Every time a function calls itself, Python places a new plate on top. When you hit the base case, you start taking plates off one by one.*
  > 
  > *Today, you will write your first recursive algorithms, master the Tower of Hanoi, and discover the built-in standard library tools (`os`, `math`, `random`, `datetime`) that make Python the #1 language in the world!"*
""")

write_f("Day-03_Recursion_Modules_StdLib/student_cheatsheets/quick_reference_card.md", """
# Day 3 Quick Reference Card: Recursion & Modules

### 1. Recursion Checklist
1. Base Case: `if n <= 1: return 1`
2. Recursive Step: `return n * factorial(n - 1)`
3. Caching: `@functools.lru_cache(maxsize=None)`

### 2. Standard Library Quick Tools
* `import math`: `sqrt`, `ceil`, `floor`, `gcd`, `pi`
* `import os`: `os.listdir()`, `os.path.exists()`, `os.path.join()`
* `import random`: `randint(1, 10)`, `choice(list)`, `shuffle(list)`
* `from datetime import datetime`: `datetime.now().strftime("%Y-%m-%d")`
""")

write_f("Day-03_Recursion_Modules_StdLib/student_lab_practice/solutions_and_code/solution_day03_all.py", """
# solution_day03_all.py
# Solutions for Day 3 Practice Problems
import os
import math

def recursive_sum(nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(nums[1:])

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x: return mid
        elif arr[mid] > x: return binary_search_recursive(arr, low, mid - 1, x)
        else: return binary_search_recursive(arr, mid + 1, high, x)
    return -1

print("Recursive Sum of [1..5]:", recursive_sum([1, 2, 3, 4, 5]))
""")

# ==============================================================================
# DAY 4
# ==============================================================================
write_f("Day-04_Exceptions_File_Handling/interview_and_exam_qa/day04_exam_and_interview_qa.md", """
# Day 4: Exam & Interview Q&A (BCSG0072)

### Q1: Why is the `with` statement preferred when opening files in Python? (5 Marks)
* **Answer**: The `with` statement utilizes Python's Context Manager protocol (`__enter__` and `__exit__`). It guarantees that the file stream is safely flushed and closed as soon as execution leaves the block, even if an unhandled runtime exception or crash occurs inside the block, preventing resource leaks.

### Q2: What is the difference between `seek()` and `tell()` methods in file handling? (3 Marks)
* **Answer**: `tell()` returns the current byte position of the file pointer within the stream. `seek(offset, whence)` moves the file pointer to a specified byte position, allowing random-access reading or writing.
""")

write_f("Day-04_Exceptions_File_Handling/presentation_scripts/trainer_speaking_script.md", """
# Day 4 Speaking Script: Shivam Gupta

### ⏰ 09:00 AM - 09:20 AM: Crash-Proof Code
* **Say**:
  > *"Up until today, whenever your code had an error, the program crashed with a red traceback. In the real world, if an ATM machine crashes when someone types a wrong PIN, that's a disaster.*
  > 
  > *Today, we learn Exception Handling (`try-except`) to make our programs bulletproof, and File Handling (`with open()`) so that when your computer turns off, your student data and bank records are safely stored on the hard disk!"*
""")

write_f("Day-04_Exceptions_File_Handling/student_cheatsheets/quick_reference_card.md", """
# Day 4 Quick Reference Card: Exceptions & Files

### 1. Exception Handling Architecture
```python
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print("Bad input:", e)
else:
    print("Computed successfully:", result)
finally:
    print("Guaranteed cleanup")
```

### 2. File I/O Cheat Table
* `'r'`: Read only (file must exist)
* `'w'`: Overwrite write (creates new / wipes existing)
* `'a'`: Append to end of file
* Syntax: `with open("file.txt", "r", encoding="utf-8") as f:`
""")

write_f("Day-04_Exceptions_File_Handling/student_lab_practice/solutions_and_code/solution_day04_all.py", """
# solution_day04_all.py
# Solutions for Day 4 Practice Problems

def safe_divide():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print(f"Result: {a / b:.2f}")
    except ZeroDivisionError:
        print("[!] Error: Cannot divide by zero!")
    except ValueError:
        print("[!] Error: Please enter numeric values!")

def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            lines = text.count('\\n') + 1
            words = len(text.split())
            chars = len(text)
            print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
    except FileNotFoundError:
        print(f"[!] File '{filename}' does not exist.")
""")

# ==============================================================================
# DAY 5
# ==============================================================================
write_f("Day-05_Regex_Projects_Database/interview_and_exam_qa/day05_exam_and_interview_qa.md", """
# Day 5: Exam & Interview Q&A (BCSG0072)

### Q1: What is the difference between `re.match()` and `re.search()`? (3 Marks)
* **Answer**: `re.match()` checks for a match only at the beginning of the string. If the pattern does not match the first character, it returns `None`. `re.search()` scans the entire string from left to right and returns the first match found anywhere in the string.

### Q2: Write a regular expression to validate an Indian Mobile Number. (3 Marks)
* **Answer**: `^[6-9]\\d{9}$`. Explanation: `^` asserts start of string; `[6-9]` ensures the first digit is 6, 7, 8, or 9; `\\d{9}` matches exactly 9 subsequent digits; `$` asserts end of string.
""")

write_f("Day-05_Regex_Projects_Database/presentation_scripts/trainer_speaking_script.md", """
# Day 5 Speaking Script: Shivam Gupta

### ⏰ 09:00 AM - 09:20 AM: The Capstone Showcase
* **Say**:
  > *"Batch B4, congratulations on reaching Day 5! Over the last 4 days, you learned variables, loops, collections, functions, recursion, exceptions, and files.*
  > 
  > *Today is the day you become software creators. Today, you are building and shipping full terminal projects: Smart Contact Books, ATM Simulators, and Quiz Engines. When you leave the lab today, you won't just have theory notes—you will have working software you built yourself!"*
""")

write_f("Day-05_Regex_Projects_Database/student_cheatsheets/quick_reference_card.md", """
# Day 5 Quick Reference Card: Regex & Database

### 1. Regex Metacharacters
* `^` (Start), `$` (End), `.` (Any char)
* `\\d` (Digit), `\\w` (Word char), `\\s` (Space)
* `*` (0+), `+` (1+), `?` (0 or 1), `{min, max}`
* `re.search(pat, text)`, `re.findall(pat, text)`, `re.sub(pat, repl, text)`

### 2. SQLite3 Quick Pattern
```python
import sqlite3
conn = sqlite3.connect("app.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
conn.commit()
conn.close()
```
""")

write_f("Day-05_Regex_Projects_Database/student_lab_practice/solutions_and_code/solution_day05_all.py", """
# solution_day05_all.py
# Solutions for Day 5 Practice Problems
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    return bool(re.match(r"^[6-9]\\d{9}$", phone))

print("Email 'student@gla.ac.in' Valid:", validate_email("student@gla.ac.in"))
print("Phone '9876543210' Valid:", validate_phone("9876543210"))
""")

print("ALL remaining subfolders populated successfully!")
