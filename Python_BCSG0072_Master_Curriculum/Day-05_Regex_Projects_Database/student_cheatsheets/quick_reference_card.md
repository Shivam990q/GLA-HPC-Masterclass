# Day 5 Quick Reference Card: Regex & Database

### 1. Regex Metacharacters
* `^` (Start), `$` (End), `.` (Any char)
* `\d` (Digit), `\w` (Word char), `\s` (Space)
* `*` (0+), `+` (1+), `?` (0 or 1), `{min, max}`
* `re.search(pat, text)`, `re.findall(pat, text)`, `re.sub(pat, repl, text)`

### 2. SQLite3 Quick Pattern
```python
import sqlite3
conn = sqlite3.connect("app.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)")
conn.commit()
conn.close()
```
