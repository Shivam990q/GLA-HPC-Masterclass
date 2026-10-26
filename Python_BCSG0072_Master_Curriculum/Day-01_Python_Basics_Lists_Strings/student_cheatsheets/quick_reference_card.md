# Day 1 Quick Reference Card: Basics, Lists & Strings

### 1. Slicing Syntax
`sequence[start:stop:step]`
* `s[1:5]` -> Indices 1, 2, 3, 4
* `s[:4]`  -> First 4 elements
* `s[2:]`  -> From index 2 to end
* `s[::-1]` -> Reversed sequence
* `s[::2]`  -> Every 2nd element

### 2. Core List Operations
* `lst.append(x)` / `lst.extend([a, b])` / `lst.insert(idx, x)`
* `lst.pop()` / `lst.remove(value)` / `lst.clear()`
* `lst.sort()` / `lst.reverse()` / `len(lst)` / `sum(lst)`
* List Comprehension: `[x*2 for x in nums if x > 0]`

### 3. Core String Methods
* `.strip()`, `.split(',')`, `','.join(list)`
* `.upper()`, `.lower()`, `.title()`, `.capitalize()`
* `.find('sub')` (returns -1), `.index('sub')` (raises ValueError)
* `.startswith('prefix')`, `.endswith('suffix')`
* F-String: `f"Name: {name}, Score: {score:.2f}"`
