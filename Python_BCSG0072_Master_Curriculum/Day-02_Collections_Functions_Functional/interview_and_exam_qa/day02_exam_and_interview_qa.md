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
