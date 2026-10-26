# Day 3 Quick Reference Card: Recursion & Modules

### 1. Recursion Checklist
1. Base Case: `if n <= 1: return 1`
2. Recursive Step: `return n * factorial(n - 1)`
3. Caching: `@functools.lru_cache(maxsize=None)`

### 2. Standard Library Quick Tools
* `import math`: `sqrt`, `ceil`, `floor`, `gcd`, `pi`
* `import os`: `os.listdir()`, `os.path.exists()`, `os.path.join()`
* `import random`: `randint(1, 10)`, `choice(list)`, `shuffle(list)`
* `from datetime import datetime`: `datetime.now().strftime("%Y-%m-%d")`
