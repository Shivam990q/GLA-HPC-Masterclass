# Day 4 Quick Reference Card: Exceptions & Files

### 1. Exception Handling Architecture
```python
try:
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print("Bad input:", e)
else:
    print("Computed successfully:", result)
finally:
    print("Guaranteed cleanup")
```

### 2. File I/O Cheat Table
* `'r'`: Read only (file must exist)
* `'w'`: Overwrite write (creates new / wipes existing)
* `'a'`: Append to end of file
* Syntax: `with open("file.txt", "r", encoding="utf-8") as f:`
