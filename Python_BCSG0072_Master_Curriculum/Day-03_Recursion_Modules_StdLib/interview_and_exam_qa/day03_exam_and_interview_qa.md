# Day 3: Exam & Interview Q&A (BCSG0072)

### Q1: What causes a Stack Overflow in recursion, and how does Python protect against it? (5 Marks)
* **Answer**: Each recursive call adds a stack frame to the system call stack. If the base case is missing or unreachable, infinite recursive calls consume all allocated stack memory, leading to stack overflow. Python protects against this via a recursion limit (default 1000), raising a `RecursionError` when exceeded.

### Q2: What is the significance of `if __name__ == '__main__':` in Python modules? (3 Marks)
* **Answer**: `__name__` is a built-in variable. When a script is executed directly, `__name__` is set to `'__main__'`. When the script is imported as a module into another file, `__name__` is set to the module's filename. This construct ensures that executable demonstration code runs only when the file is run directly, not when imported.
