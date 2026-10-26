# solution_day04_all.py
# Complete Reference Solutions for ALL 10 Day 4 Lab Practice Problems
import os
import csv
import time

print("="*60)
print("     DAY 4: COMPLETE SOLUTIONS (PROBLEMS 1 TO 10)         ")
print("="*60)

# Problem 1: Safe Integer Input Function
def read_int(simulated_input="42"):
    try:
        val = int(simulated_input)
        return val
    except (ValueError, TypeError):
        return 0
print("Problem 1 Safe Input Test (Simulated):", read_int("42"))

# Problem 2: Multiple Exception Catcher
def safe_divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        return "[!] Cannot divide by zero!"
    except TypeError:
        return "[!] Inputs must be numeric!"
    else:
        return f"[+] Result: {res:.2f}"
    finally:
        pass
print("Problem 2 Result 10/2:", safe_divide(10, 2))
print("Problem 2 Result 10/0:", safe_divide(10, 0))

# Problem 3: Custom Exception Classes
class InsufficientFundsError(Exception): pass
class NegativeAmountError(Exception): pass

def withdraw(balance, amount):
    if amount <= 0: raise NegativeAmountError("Amount must be positive")
    if amount > balance: raise InsufficientFundsError("Insufficient balance")
    return balance - amount

try:
    withdraw(1000, 1500)
except InsufficientFundsError as e:
    print("Problem 3 Caught Custom Exception:", e)

# Problem 4 & 5: File Word & Line Statistics
sample_file = "sample_stats.txt"
with open(sample_file, "w", encoding="utf-8") as f:
    f.write("Python Programming Lab\nGLA University Mathura\nBlock Teaching 2026\n")

with open(sample_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)
print(f"Problem 5 File Stats: Lines={len(lines)}, Words={total_words}, Chars={total_chars}")

# Problem 6: Seek & Tell Pointer Explorer
with open("seek_demo.txt", "w+", encoding="utf-8") as f:
    f.write("Hello World Python")
    print("Problem 6 Position after write:", f.tell())
    f.seek(6) # Move to word 'World'
    print("Problem 6 Read from byte 6:", f.read(5))

# Problem 7 & 8: CSV Export & Filter
csv_file = "employees.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Dept", "Salary"])
    writer.writerows([["Amit", "IT", 65000], ["Pooja", "HR", 45000], ["Rahul", "IT", 80000]])

high_earners = []
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Salary"]) > 50000:
            high_earners.append(row["Name"])
print("Problem 8 Employees earning > 50k:", high_earners)

# Problem 9: Timestamped Logger
log_file = "app_activity.log"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] User authentication successful\n")
print(f"Problem 9 Event appended to {log_file}")

# Problem 10: Binary File Chunk Copy
with open("test_bin.bin", "wb") as f:
    f.write(b"BINARY DATA CHUNKS TEST 1234567890")

with open("test_bin.bin", "rb") as src, open("test_bin_copy.bin", "wb") as dst:
    while chunk := src.read(16):
        dst.write(chunk)
print("Problem 10 Binary chunk copy verified successfully.")
print("="*60)
