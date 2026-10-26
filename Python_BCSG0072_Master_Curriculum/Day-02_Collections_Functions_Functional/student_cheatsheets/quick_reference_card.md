# Day 2 Quick Reference Card: Collections & Functions

### 1. Dictionary & Set Quick Syntax
* `dict.get(k, default)` / `dict.keys()` / `dict.values()` / `dict.items()`
* Dict Comprehension: `{k: v for k, v in pairs if condition}`
* Set Algebra: `s1 | s2` (Union), `s1 & s2` (Intersection), `s1 - s2` (Difference)

### 2. Functional Tools
* `lambda x, y: x + y`
* `map(func, iterable)`
* `filter(predicate, iterable)`
* `from functools import reduce; reduce(lambda a, b: a * b, [1, 2, 3, 4])`
