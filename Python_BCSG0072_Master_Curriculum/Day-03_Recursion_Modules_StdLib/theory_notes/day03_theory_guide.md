# Day 3: Recursion, Call Stack Mechanics, Modules & The Standard Library

---

### 1. Recursion First Principles
- **Definition**: A function calling itself directly or indirectly to solve smaller instances of the same problem.
- **The Two Mandatory Components**:
  1. **Base Case**: The termination condition that returns a value without making further recursive calls.
  2. **Recursive Step**: Calling the function with an altered argument that moves closer to the base case.
- **The Call Stack Under the Hood**:
  - Each recursive call pushes a new **Stack Frame** (activation record) containing local variables and return address onto the call stack.
  - When base case is met, stack frames begin **unwinding** (popping) and returning values.
  - **Stack Overflow**: Exceeding the maximum recursion depth. Inspect with `sys.getrecursionlimit()` and set with `sys.setrecursionlimit()`.
- **Recursion vs Iteration**:
  - Iteration uses fixed memory; recursion uses $O(N)$ stack memory.
  - Tree-like structures (DOM, File systems, JSON, ASTs) are naturally recursive.

---

### 2. Classic Recursive Problems
- Factorial: $F(N) = N \times F(N-1)$
- Fibonacci: $Fib(N) = Fib(N-1) + Fib(N-2)$ ($O(2^N)$ naive vs $O(N)$ memoized).
- Binary Search: Divide and conquer in $O(\log N)$.
- Tower of Hanoi: Recurrence relation $T(N) = 2T(N-1) + 1 \to 2^N - 1$ steps.
- **Memoization**:
  - Manual caching using dictionary.
  - Standard library: `@functools.lru_cache(maxsize=None)`.

---

### 3. Modules & Package Architecture
- Creating `.py` modules and import styles:
  `import math`, `from math import sqrt, pi`, `import numpy as np`.
- The `__name__ == '__main__'` idiom: Prevents script execution when imported as a library.
- Packages: Hierarchical directories containing an `__init__.py` file.

---

### 4. The Python Standard Library Toolbelt
- **`math` (12 Core Functions)**:
  `sqrt()`, `pow()`, `ceil()`, `floor()`, `factorial()`, `gcd()`, `fabs()`, `log()`, `sin()`, `cos()`, `pi`, `e`.
- **`time` (8 Core Functions)**:
  `time()`, `sleep()`, `ctime()`, `localtime()`, `gmtime()`, `strftime()`, `mktime()`, `perf_counter()`.
- **`os` (12 Core Functions)**:
  `getcwd()`, `listdir()`, `mkdir()`, `makedirs()`, `rmdir()`, `remove()`, `rename()`, `path.exists()`, `path.join()`, `path.isfile()`, `path.isdir()`, `path.getsize()`.
- **`random`**:
  `random()`, `randint(a, b)`, `choice(seq)`, `shuffle(list)`, `sample(seq, k)`, `seed(val)`.
- **`datetime`**:
  `date.today()`, `datetime.now()`, `timedelta` date arithmetic.
- **Introduction to `numpy`**:
  Vectorized arrays, `np.arange()`, `np.reshape()`, `np.mean()`, `np.sum()`.
