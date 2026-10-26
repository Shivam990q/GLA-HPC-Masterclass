# Day 1: OOPS Exam & Top Placement Interview Q&A

### Q1: What is Method Resolution Order (MRO) and how does Python's C3 Linearization work?
- **Answer**: MRO defines the order in which base classes are searched when executing a method on an object. Python uses the **C3 Linearization Algorithm**, which guarantees two properties:
  1. Children precede their parents.
  2. If class $B$ precedes class $C$ in the subclass declaration `class D(B, C)`, then $B$ precedes $C$ throughout the resolution order.

### Q2: What is Name Mangling in Python?
- **Answer**: When an identifier starts with two or more leading underscores (`__pin`), Python rewrites the attribute name internally by prefixing `_ClassName` (e.g. `_BankAccount__pin`). This is designed to prevent accidental namespace collisions in inheritance subclasses. It is not true security (it can still be accessed via `_ClassName__var`), but it enforces encapsulation conventions.

### Q3: What is the difference between `@staticmethod` and `@classmethod`?
- **Answer**:
  - `@classmethod` takes `cls` as its first argument and can access/modify class-level state. Useful for factory methods (alternative constructors like `from_dict()`).
  - `@staticmethod` takes neither `self` nor `cls`. It is a plain function scoped inside the class namespace for organizational clarity.
