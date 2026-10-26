# demo_functional_pipelines.py
# Functional Programming: Lambda, Map, Filter, Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original Numbers:", numbers)

# 1. Filter: Extract even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Filtered Evens:", evens)

# 2. Map: Square each even number
squared_evens = list(map(lambda x: x**2, evens))
print("Mapped Squares:", squared_evens)

# 3. Reduce: Compute sum of squares
sum_of_squares = reduce(lambda acc, x: acc + x, squared_evens)
print("Reduced Sum of Squares:", sum_of_squares)

# 4. The Functional Pipeline in One Single Expression
pipeline_result = reduce(lambda a, b: a + b, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("Pipeline One-Liner Result:", pipeline_result)

# 5. Contrast with List Comprehension equivalent
comp_result = sum([x**2 for x in numbers if x % 2 == 0])
print("List Comprehension Equivalent:", comp_result)
