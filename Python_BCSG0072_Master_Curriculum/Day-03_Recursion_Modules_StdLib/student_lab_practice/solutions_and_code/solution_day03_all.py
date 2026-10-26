# solution_day03_all.py
# Complete Reference Solutions for ALL 10 Day 3 Lab Practice Problems
import math
import os
import random
from datetime import datetime, timedelta

print("="*60)
print("     DAY 3: COMPLETE SOLUTIONS (PROBLEMS 1 TO 10)         ")
print("="*60)

# Problem 1: Sum of Digits via Recursion
def sum_digits(n):
    if n == 0: return 0
    return (n % 10) + sum_digits(n // 10)
print("Problem 1 Sum of Digits (12345):", sum_digits(12345))

# Problem 2: Fast Recursive Exponentiation (O(log Y))
def fast_power(x, y):
    if y == 0: return 1
    half = fast_power(x, y // 2)
    if y % 2 == 0: return half * half
    return x * half * half
print("Problem 2 Fast Power 2^10:", fast_power(2, 10))

# Problem 3: Recursive GCD (Euclidean)
def recursive_gcd(a, b):
    if b == 0: return a
    return recursive_gcd(b, a % b)
print("Problem 3 Recursive GCD(48, 180):", recursive_gcd(48, 180))

# Problem 4: Recursive String Reversal
def reverse_str(s):
    if len(s) <= 1: return s
    return s[-1] + reverse_str(s[:-1])
print("Problem 4 Reverse 'GLA University':", reverse_str("GLA University"))

# Problem 5: Recursive List Sum and Max
def rec_list_sum(lst):
    if not lst: return 0
    return lst[0] + rec_list_sum(lst[1:])

def rec_list_max(lst):
    if len(lst) == 1: return lst[0]
    sub_max = rec_list_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max
print("Problem 5 List Sum:", rec_list_sum([10, 20, 30, 40]))
print("Problem 5 List Max:", rec_list_max([10, 45, 20, 89, 34]))

# Problem 6: Recursive Binary Search
def rec_binary_search(arr, target, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    elif arr[mid] > target: return rec_binary_search(arr, target, low, mid - 1)
    else: return rec_binary_search(arr, target, mid + 1, high)
sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Problem 6 Binary Search Index of 23:", rec_binary_search(sorted_arr, 23, 0, len(sorted_arr)-1))

# Problem 7: Recursive Character Counter
def count_char(s, ch):
    if not s: return 0
    return (1 if s[0] == ch else 0) + count_char(s[1:], ch)
print("Problem 7 Count 'a' in 'abracadabra':", count_char("abracadabra", 'a'))

# Problem 8: Date Arithmetic
now = datetime.now()
target_event = now + timedelta(days=45, hours=12)
diff = target_event - now
print(f"Problem 8 Countdown: {diff.days} days, {diff.seconds//3600} hours remaining")

# Problem 9: OS Directory Scan
txt_files = [f for f in os.listdir('.') if f.endswith('.py')]
print(f"Problem 9 Detected Python Files in CWD ({len(txt_files)} files):", txt_files[:3])

# Problem 10: Dice Simulator (P(Sum = 7))
rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(1000)]
sevens = rolls.count(7)
print(f"Problem 10 Frequency of 7 in 1000 rolls: {sevens}/1000 ({sevens/10:.1f}%) [Theory: ~16.7%]")
print("="*60)
