# Day 4: Exam & Interview Q&A (BCSG0072)

### Q1: Why is the `with` statement preferred when opening files in Python? (5 Marks)
* **Answer**: The `with` statement utilizes Python's Context Manager protocol (`__enter__` and `__exit__`). It guarantees that the file stream is safely flushed and closed as soon as execution leaves the block, even if an unhandled runtime exception or crash occurs inside the block, preventing resource leaks.

### Q2: What is the difference between `seek()` and `tell()` methods in file handling? (3 Marks)
* **Answer**: `tell()` returns the current byte position of the file pointer within the stream. `seek(offset, whence)` moves the file pointer to a specified byte position, allowing random-access reading or writing.
