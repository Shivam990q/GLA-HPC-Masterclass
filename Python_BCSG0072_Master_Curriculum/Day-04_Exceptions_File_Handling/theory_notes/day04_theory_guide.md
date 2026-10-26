# Day 4: Defensive Coding, Exception Architecture & Persistent File I/O

---

### 1. Errors vs Exceptions
- **Syntax Errors**: Parsing stage failures (invalid indentation, missing colons). Program does not start.
- **Runtime Exceptions**: Logical failures during execution. Unhandled exceptions crash the program with a traceback.
- **Common Standard Exceptions**:
  `ZeroDivisionError`, `ValueError`, `TypeError`, `IndexError`, `KeyError`, `FileNotFoundError`, `AttributeError`.

---

### 2. The Complete Exception Handling Block
```python
try:
    # Risky code
    value = 10 / divisor
except ZeroDivisionError as e:
    # Catches specific error
    print("Cannot divide by zero")
except (ValueError, TypeError) as e:
    # Catches multiple errors
    print("Invalid data type or value")
else:
    # Executes ONLY if NO exception was raised in try block
    print("Success! Result is:", value)
finally:
    # GUARANTEED to execute (ideal for closing files / db connections)
    print("Cleanup complete.")
```

- **Raising Exceptions**: `raise ValueError("Age must be >= 18")`
- **Assertions**: `assert condition, "Error message"`
- **Custom User-Defined Exceptions**:
  ```python
  class InsufficientFundsError(Exception):
      """Raised when account balance is lower than withdrawal amount."""
      pass
  ```

---

### 3. File Handling Mechanics
- File Streams and Context Managers:
  ```python
  with open("data.txt", "w", encoding="utf-8") as file:
      file.write("Hello World")
  # File automatically closed, even if an exception occurs inside!
  ```
- **File Modes**:
  `'r'` (Read), `'w'` (Write/Overwrite), `'a'` (Append), `'r+'` (Read/Write), `'rb'` / `'wb'` (Binary modes).
- **The 10 Core Stream Methods**:
  1. `read([size])`: Reads entire content or specified bytes.
  2. `readline()`: Reads single line including `\n`.
  3. `readlines()`: Reads all lines into a list of strings.
  4. `write(str)`: Writes string to stream.
  5. `writelines(list)`: Writes sequence of strings.
  6. `seek(offset, whence)`: Moves file pointer to byte position.
  7. `tell()`: Returns current byte offset of file pointer.
  8. `flush()`: Forces buffer flush to physical disk.
  9. `close()`: Closes stream and releases OS file handle.
  10. `truncate([size])`: Truncates file to specified byte size.
