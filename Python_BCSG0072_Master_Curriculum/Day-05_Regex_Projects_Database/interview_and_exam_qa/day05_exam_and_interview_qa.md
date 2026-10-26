# Day 5: Exam & Interview Q&A (BCSG0072)

### Q1: What is the difference between `re.match()` and `re.search()`? (3 Marks)
* **Answer**: `re.match()` checks for a match only at the beginning of the string. If the pattern does not match the first character, it returns `None`. `re.search()` scans the entire string from left to right and returns the first match found anywhere in the string.

### Q2: Write a regular expression to validate an Indian Mobile Number. (3 Marks)
* **Answer**: `^[6-9]\d{9}$`. Explanation: `^` asserts start of string; `[6-9]` ensures the first digit is 6, 7, 8, or 9; `\d{9}` matches exactly 9 subsequent digits; `$` asserts end of string.
