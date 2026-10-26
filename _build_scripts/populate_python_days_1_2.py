# populate_python_days_1_2.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\Python_BCSG0072_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 1: PYTHON BASICS, LISTS & STRINGS
# ==============================================================================
write_f("Day-01_Python_Basics_Lists_Strings/theory_notes/day01_theory_guide.md", """
# Day 1: Python Basics, Control Flow, Lists & Strings
## Comprehensive Lecture & Whiteboard Guide

---

### 1. Python Architecture & Mental Models
- **Compiled to Bytecode (.pyc) -> Interpreted by CPython Virtual Machine (PVM)**.
- **Dynamic Typing**: Variables do not store types; values do. A variable is simply a pointer/reference to an object in memory (`id(x)`).
- **Mutable vs Immutable**:
  - Immutable: `int`, `float`, `str`, `tuple`, `bool`. Modifying creates a new object in memory.
  - Mutable: `list`, `dict`, `set`. Modifying alters the object in-place without changing memory address.

---

### 2. Conditionals & Decision Making
- `if`, `if-else`, `elif`, nested `if`.
- **Ternary Operator (Conditional Expression)**:
  `result = value_if_true if condition else value_if_false`
- Truthy vs Falsy values: `0`, `0.0`, `""`, `[]`, `()`, `{}`, `None`, `False` are all Falsy. Everything else is Truthy.

---

### 3. Iteration & Loop Architecture
- `for` loop (Iterating over sequences/iterables using `range(start, stop, step)`).
- `while` loop (Condition-driven execution).
- Loop Control Statements:
  - `break`: Terminate loop completely.
  - `continue`: Skip remaining code in current iteration and jump to next.
  - `pass`: Syntactic no-op placeholder.
- **The `for-else` & `while-else` Construct**:
  - The `else` block executes **only if the loop finishes naturally without encountering a `break` statement** (ideal for search algorithms).

---

### 4. Lists In-Depth (Array Mechanics in Python)
- Dynamic arrays storing references to objects.
- Indexing: Positive (`0` to `n-1`) and Negative (`-1` to `-n`).
- Slicing: `list[start:stop:step]` (e.g. `list[::-1]` reverses in $O(N)$).
- **The 15 Core List Methods & Functions**:
  1. `append(x)`: Adds item to end ($O(1)$ amortized).
  2. `extend(iterable)`: Appends elements from iterable ($O(K)$).
  3. `insert(i, x)`: Inserts element at index $i$ ($O(N)$ shift).
  4. `remove(x)`: Removes first occurrence of value $x$ (Raises `ValueError` if not found).
  5. `pop([i])`: Removes and returns item at index $i$ (default last element, $O(1)$).
  6. `clear()`: Empties the list.
  7. `index(x)`: Returns index of first occurrence.
  8. `count(x)`: Returns frequency of element.
  9. `sort(key=None, reverse=False)`: In-place Timsort ($O(N \\log N)$).
  10. `reverse()`: Reverses list in-place ($O(N)$).
  11. `copy()`: Returns shallow copy.
  12. `len(list)`: Returns element count ($O(1)$ attribute read).
  13. `sum(list)`: Returns numeric sum.
  14. `min(list)`: Returns minimum element.
  15. `max(list)`: Returns maximum element.
- **List Comprehensions**:
  `[expression for item in iterable if condition]`
  - Nested comprehensions: Flattening 2D matrices.

---

### 5. Strings In-Depth (Immutability & String Algorithms)
- Sequence of Unicode characters.
- String immutability: Cannot do `s[0] = 'A'`. Must construct a new string.
- **The 18 Core String Methods**:
  `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`, `strip()`, `lstrip()`, `rstrip()`, `split()`, `join()`, `replace()`, `find()`, `index()`, `count()`, `startswith()`, `endswith()`, `isdigit()`, `isalpha()`.
- Additional inspection methods: `isalnum()`, `isspace()`, `center()`, `zfill()`, `partition()`.
- Modern String Formatting: F-strings `f"{val:.2f}"`.
""")

write_f("Day-01_Python_Basics_Lists_Strings/live_demo/demo_basics_and_loops.py", """
# demo_basics_and_loops.py
# Run this live in class to demonstrate Conditionals, Loops, and Loop-Else

print("="*60)
print("     DEMO 1: CONDITIONALS & TERNARY EXPRESSIONS           ")
print("="*60)

marks = 85
# Clean Ternary Operator
grade = "Distinction" if marks >= 75 else "Pass"
print(f"Marks: {marks} -> Status: {grade}")

print("\\n" + "="*60)
print("     DEMO 2: THE FOR-ELSE PRIME SEARCH ALGORITHM          ")
print("="*60)

num = 29
# Demonstrating loop-else: 'else' runs ONLY if no 'break' was hit
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f"{num} is composite (divisible by {i})")
        break
else:
    print(f"{num} is PRIME! (Loop finished without hitting break)")

print("\\n" + "="*60)
print("     DEMO 3: NESTED LOOPS & PATTERN PRINTING              ")
print("="*60)
# Pyramid live demo
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
""")

write_f("Day-01_Python_Basics_Lists_Strings/live_demo/demo_lists_mastery.py", """
# demo_lists_mastery.py
# Complete demonstration of all 15 List Methods and List Comprehensions

print("="*60)
print("           MASTERING ALL 15 LIST METHODS                  ")
print("="*60)

numbers = [10, 20, 30, 40]
print("Initial List:", numbers)

# 1. append
numbers.append(50)
# 2. extend
numbers.extend([60, 70])
# 3. insert
numbers.insert(2, 25) # Insert 25 at index 2
print("After Append, Extend, Insert:", numbers)

# 4. remove
numbers.remove(25)
# 5. pop
popped = numbers.pop() # Pops 70
print(f"Popped element: {popped} | List: {numbers}")

# 6. index, 7. count
print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))

# 8. sort, 9. reverse
numbers.sort(reverse=True)
print("Sorted descending:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# 10. Built-in functions: len, sum, min, max
print(f"Len: {len(numbers)}, Sum: {sum(numbers)}, Min: {min(numbers)}, Max: {max(numbers)}")

# 11. List Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [val for row in matrix for val in row if val % 2 == 0]
print("Even numbers from flattened matrix:", flattened)

# 12. Slicing tricks
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Reversed via slicing [::-1]:", nums[::-1])
print("Every second element [::2]:", nums[::2])
""")

write_f("Day-01_Python_Basics_Lists_Strings/student_lab_practice/day01_practice_sheet.md", """
# Day 1: Student Practice Problem Set (10 Graded Problems)
**Target**: Complete all 10 problems in the lab before 04:30 PM.

1. **Temperature Converter**: Write a program taking Celsius input and printing Fahrenheit with 2 decimal precision using an f-string.
2. **Second Largest Element**: Given a list of integers, find the second largest element without using the `sort()` method.
3. **List Deduplicator**: Write a program to remove all duplicate elements from a list while maintaining the original order.
4. **Palindrome Slicer**: Take a string input, strip whitespace, convert to lowercase, and check if it is a palindrome using slice notation `[::-1]`.
5. **Vowel and Consonant Counter**: Write a program that takes a sentence and counts total vowels, consonants, digits, and spaces using string inspection methods.
6. **Matrix Transpose via Comprehension**: Given a 3x3 matrix, compute its transpose in a single line of list comprehension.
7. **Title Case Converter without `.title()`**: Capitalize the first letter of each word in a string using `.split()` and `.capitalize()`.
8. **Word Frequency Counter**: Given a paragraph, clean punctuation and count occurrences of each word stored in parallel lists.
9. **Even-Odd Sorter**: Separate a list of numbers into even and odd lists using list comprehensions.
10. **Password Strength Checker**: Validate if a password has at least 8 characters, contains at least 1 digit (`.isdigit()`), and contains at least 1 alphabet (`.isalpha()`).
""")

write_f("Day-01_Python_Basics_Lists_Strings/student_lab_practice/solutions_and_code/solution_day01_all.py", """
# solution_day01_all.py
# Reference Solutions for all 10 Day 1 Lab Practice Problems

# 1. Temperature Converter
celsius = 37.5
fahrenheit = (celsius * 9/5) + 32
print(f"Problem 1: {celsius}C = {fahrenheit:.2f}F")

# 2. Second Largest Element (Without sort)
nums = [12, 45, 2, 45, 89, 34, 89, 21]
first = second = float('-inf')
for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n
print("Problem 2 Second Largest:", second)

# 3. List Deduplicator (Preserving Order)
raw_list = [1, 2, 2, 3, 4, 3, 5, 1]
deduped = []
for x in raw_list:
    if x not in deduped:
        deduped.append(x)
print("Problem 3 Deduplicated:", deduped)

# 4. Palindrome Check
text = "A man a plan a canal Panama".replace(" ", "").lower()
is_palin = text == text[::-1]
print("Problem 4 Is Palindrome:", is_palin)

# 5. Matrix Transpose
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in mat] for i in range(len(mat[0]))]
print("Problem 6 Transpose:", transposed)
""")

write_f("Day-01_Python_Basics_Lists_Strings/interview_and_exam_qa/day01_exam_and_interview_qa.md", """
# Day 1: University Examination & Technical Interview Q&A

### Q1: What is the difference between mutable and immutable data types in Python? (5 Marks)
* **Answer**: In Python, an immutable object's state/value cannot be modified after creation (`int`, `float`, `str`, `tuple`). Any operation that appears to modify an immutable object allocates a new object in memory. A mutable object (`list`, `dict`, `set`) allows modifying elements in-place without altering the underlying memory address (`id()`).

### Q2: How does Python's `for-else` statement work? Give an example. (3 Marks)
* **Answer**: The `else` block following a `for` loop executes only if the loop completes all iterations normally without being interrupted by a `break` statement. If a `break` is encountered, the `else` block is skipped entirely. This is used in search algorithms to detect when an item is not found.

### Q3: Explain the difference between `list.append()` and `list.extend()`. (2 Marks)
* **Answer**: `append(x)` adds its argument as a single element to the end of the list, increasing length by 1. `extend(iterable)` iterates over its argument and appends each element individually, increasing length by `len(iterable)`.

### Q4: What is the time complexity of `list.insert(0, x)` vs `list.append(x)`?
* **Answer**: `append(x)` is $O(1)$ amortized time because it adds to the end of the dynamic array. `insert(0, x)` is $O(N)$ time because every existing element in the array must be shifted one index to the right in memory.

### Q5: What is the output of `"hello"[::-1]` and how does it work? (2 Marks)
* **Answer**: Output is `"olleh"`. It uses slice notation `[start:stop:step]`. With empty start/stop and a step of `-1`, Python traverses the string backwards from the last index to the first index.
""")

write_f("Day-01_Python_Basics_Lists_Strings/student_cheatsheets/quick_reference_card.md", """
# Day 1 Quick Reference Card: Basics, Lists & Strings

### 1. Slicing Syntax
`sequence[start:stop:step]`
* `s[1:5]` -> Indices 1, 2, 3, 4
* `s[:4]`  -> First 4 elements
* `s[2:]`  -> From index 2 to end
* `s[::-1]` -> Reversed sequence
* `s[::2]`  -> Every 2nd element

### 2. Core List Operations
* `lst.append(x)` / `lst.extend([a, b])` / `lst.insert(idx, x)`
* `lst.pop()` / `lst.remove(value)` / `lst.clear()`
* `lst.sort()` / `lst.reverse()` / `len(lst)` / `sum(lst)`
* List Comprehension: `[x*2 for x in nums if x > 0]`

### 3. Core String Methods
* `.strip()`, `.split(',')`, `','.join(list)`
* `.upper()`, `.lower()`, `.title()`, `.capitalize()`
* `.find('sub')` (returns -1), `.index('sub')` (raises ValueError)
* `.startswith('prefix')`, `.endswith('suffix')`
* F-String: `f"Name: {name}, Score: {score:.2f}"`
""")

write_f("Day-01_Python_Basics_Lists_Strings/presentation_scripts/trainer_speaking_script.md", """
# Day 1 Trainer Speaking Script: Shivam Gupta

### ⏰ 09:00 AM - 09:20 AM: Welcoming Freshmen & The Hook
* **Action**: Stand tall, smile, look across the whole room. Write on the board: `x = 10`.
* **Say**:
  > *"Good morning, Batch B4! Welcome to Computer Science at GLA University!*
  > 
  > *Look at the board: `x = 10`. In C or Java, you would have to write `int x = 10;`. You have to declare types, manage memory, and put semicolons. If you miss a semicolon, the compiler shouts at you.*
  > 
  > *Python is different. Python is the language of artificial intelligence, high-performance backends, and data science. In Python, variables are not boxes that hold types—they are pointers with name tags. Over the next 5 days, we are going to master this language from the ground up.*
  > 
  > *If you have never written a line of code before, don't worry. Errors in our class are celebrated! Whenever you see a red error message, that is Python talking to you, telling you how to become a better engineer. Let's write our first script!"*
""")

# ==============================================================================
# DAY 2: COLLECTIONS, FUNCTIONS & FUNCTIONAL PROGRAMMING
# ==============================================================================
write_f("Day-02_Collections_Functions_Functional/theory_notes/day02_theory_guide.md", """
# Day 2: Tuples, Sets, Dictionaries, Functions & Functional Pipelines

---

### 1. Tuples In-Depth (Immutable Sequences)
- Defined with parentheses `()` or comma separation.
- **Why Tuples over Lists?**
  - Performance: Tuples are allocated in a single memory block; lists require over-allocation for dynamic resizing.
  - Hashability: Tuples can be used as Dictionary keys and Set elements (if all tuple items are immutable).
  - Data Integrity: Write-protects data that shouldn't change (e.g. GPS coordinates).
- Methods: `count()`, `index()`.
- Tuple Unpacking: `a, b, *rest = (1, 2, 3, 4, 5)`.

---

### 2. Sets In-Depth (Hash Table Uniqueness)
- Unordered collection of unique, hashable elements.
- Under the hood: Implemented using open-addressing Hash Tables ($O(1)$ average time complexity for lookup/insertion).
- **The 15 Core Set Methods & Operations**:
  - Insertion/Removal: `add()`, `update()`, `remove()` (raises KeyError), `discard()` (silent), `pop()`, `clear()`.
  - Set Algebra:
    - Union: `s1 | s2` or `s1.union(s2)`
    - Intersection: `s1 & s2` or `s1.intersection(s2)`
    - Difference: `s1 - s2` or `s1.difference(s2)`
    - Symmetric Difference: `s1 ^ s2` or `s1.symmetric_difference(s2)`
  - Subsets/Supersets: `issubset()`, `issuperset()`, `isdisjoint()`.

---

### 3. Dictionaries In-Depth (Key-Value Hash Maps)
- Associative key-value store. Keys must be immutable and hashable (`__hash__()`).
- Preserves insertion order (since Python 3.7+ via dense array layout).
- **The 15 Core Dictionary Methods**:
  `get(key, default)`, `keys()`, `values()`, `items()`, `update()`, `pop(key)`, `popitem()`, `setdefault()`, `clear()`, `copy()`, `fromkeys()`, `del d[k]`, `len()`, `in`, `sorted()`.
- **Dictionary Comprehensions**:
  `{k: v for k, v in iterable}`

---

### 4. Modular Functions & Variable Scope
- Defining with `def`, docstrings `\"\"\"...\"\"\"`, and `return` vs `print`.
- Parameter Types:
  1. Positional arguments.
  2. Keyword arguments.
  3. Default parameters (Caution: Never use mutable default arguments like `def f(a=[])`).
  4. Variable-length arguments: `*args` (collected into a tuple) and `**kwargs` (collected into a dictionary).
- **Variable Scope: The LEGB Rule**:
  - **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.
  - `global` keyword: Modify global state inside function.
  - `nonlocal` keyword: Modify enclosing function state in nested closures.

---

### 5. Functional Programming Tools
- **Lambda Functions**: Anonymous single-expression functions: `lambda x: x**2`.
- `map(func, iterable)`: Applies function to every element, returns an iterator.
- `filter(func, iterable)`: Filters elements where predicate returns True.
- `functools.reduce(func, iterable)`: Cumulatively applies function across items to reduce to a single value.
- **Pipelines**: Combining `map`, `filter`, and `reduce` vs List Comprehensions.
""")

write_f("Day-02_Collections_Functions_Functional/live_demo/demo_dictionaries.py", """
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
print("\\nStudent Record:")
for key, val in student.items():
    print(f"  {key.upper()}: {val}")

# Dictionary Comprehension: Grade categorization
marks = {"Aarav": 88, "Neha": 92, "Rohan": 64, "Priya": 79}
grades = {name: ("A" if m >= 90 else "B" if m >= 75 else "C") for name, m in marks.items()}
print("\\nGenerated Grades via Dict Comprehension:")
print(grades)

print("\\n" + "="*60)
print("      FUNCTION *ARGS, **KWARGS & LEGB SCOPE               ")
print("="*60)

def university_enrollment(course, *students, **metadata):
    \"\"\"Demonstrating variable arguments and kwargs.\"\"\"
    print(f"Course: {course}")
    print(f"Enrolled Students ({len(students)}): {', '.join(students)}")
    print("Metadata:", metadata)

university_enrollment("BCSG0072", "Amit", "Pooja", "Rahul", semester="1st", lab="Lab 4")
""")

write_f("Day-02_Collections_Functions_Functional/live_demo/demo_functional_pipelines.py", """
# demo_functional_pipelines.py
# Functional Programming: Lambda, Map, Filter, Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original Numbers:", numbers)

# 1. Filter: Extract even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Evens:", evens)

# 2. Map: Square each even number
squared_evens = list(map(lambda x: x**2, evens))
print("Mapped Squares:", squared_evens)

# 3. Reduce: Compute sum of squares
sum_of_squares = reduce(lambda acc, x: acc + x, squared_evens)
print("Reduced Sum of Squares:", sum_of_squares)

# 4. The Functional Pipeline in One Single Expression
pipeline_result = reduce(lambda a, b: a + b, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("Pipeline One-Liner Result:", pipeline_result)

# 5. Contrast with List Comprehension equivalent
comp_result = sum([x**2 for x in numbers if x % 2 == 0])
print("List Comprehension Equivalent:", comp_result)
""")

write_f("Day-02_Collections_Functions_Functional/student_lab_practice/day02_practice_sheet.md", """
# Day 2: Student Practice Problem Set (10 Graded Problems)

1. **Common Elements Finder**: Given two lists, use Sets to find the common elements and the elements unique to each list.
2. **Dictionary Inverter**: Write a function that inverts a dictionary (swaps keys and values). Handle duplicate values by storing keys in a list.
3. **Student Score Aggregator**: Given a list of student records `[{"name": "X", "marks": [80, 90, 85]}]`, use a dictionary comprehension to compute each student's average score.
4. **Flexible Calculator via `*args`**: Write a function `calculate(operation, *numbers)` that supports 'add', 'multiply', 'min', and 'max' over variable numbers.
5. **Word Length Mapper**: Using `map()` and `lambda`, transform a sentence into a list of word lengths.
6. **Prime Filter via `filter()`**: Use `filter()` with a lambda or helper function to filter all prime numbers from a range 1 to 100.
7. **Factorial via `reduce()`**: Calculate $N!$ using `functools.reduce` and `range()`.
8. **LEGB Scope Experimenter**: Write a script demonstrating shadowing of global variables inside nested functions using the `nonlocal` and `global` keywords.
9. **Inventory Stock Alert**: Given a dictionary of store items and quantities, filter all items with stock less than 5 using dictionary comprehension.
10. **Tuple Matrix Sorting**: Given a list of student tuples `(name, age, cgpa)`, sort the list first by CGPA descending, then by age ascending.
""")

write_f("Day-02_Collections_Functions_Functional/student_lab_practice/solutions_and_code/solution_day02_all.py", """
# solution_day02_all.py
# Reference Solutions for Day 2 Practice Problems
from functools import reduce

# 1. Set Operations
list1, list2 = [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
s1, s2 = set(list1), set(list2)
print("Common:", s1 & s2)
print("Unique to List 1:", s1 - s2)

# 2. Dictionary Inverter
original = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)
print("Inverted Dict:", inverted)

# 7. Factorial via reduce
n = 6
fact = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"Factorial of {n} via reduce: {fact}")
""")

print("Day 1 & Day 2 populated successfully.")
