# solution_day01_all.py
# Reference Solutions for all 10 Day 1 Lab Practice Problems

# 1. Temperature Converter
celsius = 37.5
fahrenheit = (celsius * 9/5) + 32
print(f"Problem 1: {celsius}C = {fahrenheit:.2f}F")

# 2. Second Largest Element (Without sort)
nums = [12, 45, 2, 45, 89, 34, 89, 21]
first = second = float('-inf')
for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n
print("Problem 2 Second Largest:", second)

# 3. List Deduplicator (Preserving Order)
raw_list = [1, 2, 2, 3, 4, 3, 5, 1]
deduped = []
for x in raw_list:
    if x not in deduped:
        deduped.append(x)
print("Problem 3 Deduplicated:", deduped)

# 4. Palindrome Check
text = "A man a plan a canal Panama".replace(" ", "").lower()
is_palin = text == text[::-1]
print("Problem 4 Is Palindrome:", is_palin)

# 5. Matrix Transpose
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in mat] for i in range(len(mat[0]))]
print("Problem 6 Transpose:", transposed)
