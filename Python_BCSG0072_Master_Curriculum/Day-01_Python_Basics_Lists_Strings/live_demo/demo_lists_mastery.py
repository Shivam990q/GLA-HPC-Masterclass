# demo_lists_mastery.py
# Complete demonstration of all 15 List Methods and List Comprehensions

print("="*60)
print("           MASTERING ALL 15 LIST METHODS                  ")
print("="*60)

numbers = [10, 20, 30, 40]
print("Initial List:", numbers)

# 1. append
numbers.append(50)
# 2. extend
numbers.extend([60, 70])
# 3. insert
numbers.insert(2, 25) # Insert 25 at index 2
print("After Append, Extend, Insert:", numbers)

# 4. remove
numbers.remove(25)
# 5. pop
popped = numbers.pop() # Pops 70
print(f"Popped element: {popped} | List: {numbers}")

# 6. index, 7. count
print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))

# 8. sort, 9. reverse
numbers.sort(reverse=True)
print("Sorted descending:", numbers)
numbers.reverse()
print("Reversed:", numbers)

# 10. Built-in functions: len, sum, min, max
print(f"Len: {len(numbers)}, Sum: {sum(numbers)}, Min: {min(numbers)}, Max: {max(numbers)}")

# 11. List Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [val for row in matrix for val in row if val % 2 == 0]
print("Even numbers from flattened matrix:", flattened)

# 12. Slicing tricks
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Reversed via slicing [::-1]:", nums[::-1])
print("Every second element [::2]:", nums[::2])
