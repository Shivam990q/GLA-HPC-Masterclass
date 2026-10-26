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
- Defining with `def`, docstrings `"""..."""`, and `return` vs `print`.
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
