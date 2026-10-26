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
  9. `sort(key=None, reverse=False)`: In-place Timsort ($O(N \log N)$).
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
