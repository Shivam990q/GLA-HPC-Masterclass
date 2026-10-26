# solution_day02_all.py
# Reference Solutions for Day 2 Practice Problems
from functools import reduce

# 1. Set Operations
list1, list2 = [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
s1, s2 = set(list1), set(list2)
print("Common:", s1 & s2)
print("Unique to List 1:", s1 - s2)

# 2. Dictionary Inverter
original = {"a": 1, "b": 2, "c": 1}
inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)
print("Inverted Dict:", inverted)

# 7. Factorial via reduce
n = 6
fact = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"Factorial of {n} via reduce: {fact}")
