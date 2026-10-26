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
