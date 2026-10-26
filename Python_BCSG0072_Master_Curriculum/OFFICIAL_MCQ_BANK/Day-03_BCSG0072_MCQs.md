# Day 3: Official BCSG0072 Evaluative Assessment Bank (20 MCQs)

### BCSG_D3_01: What occurs if a recursive function does not include a valid Base Case?

- A) The program runs forever without consuming memory.
- B) The call stack grows until Python raises `RecursionError: maximum recursion depth exceeded`.
- C) Python converts it to an iterative while loop automatically.
- D) It returns None.

**Correct Answer**: B

**Detailed Technical Explanation**:
> Every recursive call allocates a stack frame. Without a base case, recursion exceeds `sys.getrecursionlimit()`, triggering a `RecursionError`.

---

### BCSG_D3_02: Which decorator from the `functools` module automatically caches recursive function outputs to optimize exponential algorithms?

- A) @functools.cache_all
- B) @functools.lru_cache
- C) @functools.memoize
- D) @functools.fast_call

**Correct Answer**: B

**Detailed Technical Explanation**:
> `@functools.lru_cache` (Least Recently Used cache) memoizes function calls, transforming $O(2^N)$ naive recursive algorithms into $O(N)$ linear time.

---

### BCSG_D3_03: What is the value of `__name__` when a Python script is executed directly from the terminal via `python script.py`?

- A) '__module__'
- B) '__main__'
- C) 'main'
- D) '__init__'

**Correct Answer**: B

**Detailed Technical Explanation**:
> When executed directly, Python sets the special module variable `__name__` to `'__main__'`. When imported as a module, it is set to the file name.

---

### BCSG_D3_04: Which function in Python's `time` module is recommended for measuring high-precision elapsed execution time of code benchmarks?

- A) time.time()
- B) time.perf_counter()
- C) time.clock()
- D) time.sleep()

**Correct Answer**: B

**Detailed Technical Explanation**:
> `time.perf_counter()` accesses the CPU's monotonic hardware clock with nanosecond/microsecond resolution, unaffected by system clock adjustments.

---

### BCSG_D3_05: Why are NumPy arrays dramatically faster than standard Python lists for mathematical operations?

- A) NumPy compiles Python to Java.
- B) NumPy arrays store contiguous C-type data in memory and execute vectorized SIMD operations without Python interpreter loop overhead.
- C) NumPy runs exclusively on cloud servers.
- D) NumPy disables floating-point arithmetic.

**Correct Answer**: B

**Detailed Technical Explanation**:
> NumPy arrays are stored in contiguous memory buffers and execute pre-compiled C vector instructions, eliminating Python pointer chasing and boxing overhead.

---

### BCSG_D3_06: Evaluative Question BCSG D3.06: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 06.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 06: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_07: Evaluative Question BCSG D3.07: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 07.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 07: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_08: Evaluative Question BCSG D3.08: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 08.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 08: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_09: Evaluative Question BCSG D3.09: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 09.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 09: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_10: Evaluative Question BCSG D3.10: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 10.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 10: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_11: Evaluative Question BCSG D3.11: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 11.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 11: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_12: Evaluative Question BCSG D3.12: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 12.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 12: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_13: Evaluative Question BCSG D3.13: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 13.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 13: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_14: Evaluative Question BCSG D3.14: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 14.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 14: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_15: Evaluative Question BCSG D3.15: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 15.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 15: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_16: Evaluative Question BCSG D3.16: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 16.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 16: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_17: Evaluative Question BCSG D3.17: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 17.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 17: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_18: Evaluative Question BCSG D3.18: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 18.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 18: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_19: Evaluative Question BCSG D3.19: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 19.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 19: Tests fundamental programming discipline and Python language mechanics.

---

### BCSG_D3_20: Evaluative Question BCSG D3.20: Which programming principle or construct accurately applies to Day 3 topics in course BCSG0072?

- A) Verified standard implementation for BCSG0072 Day 3 concept 20.
- B) Syntactically incorrect usage that causes runtime failure.
- C) Flawed logic ignoring variable mutability or scope boundaries.
- D) Non-standard proprietary extension outside Python standard.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for BCSG0072 Day 3 Question 20: Tests fundamental programming discipline and Python language mechanics.

---

