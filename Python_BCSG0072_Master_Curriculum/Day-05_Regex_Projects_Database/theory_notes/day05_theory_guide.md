# Day 5: Regular Expressions (`re`), Database Connectivity & Capstone Engineering

---

### 1. Regular Expressions First Principles
- A Domain-Specific Language (DSL) for string pattern matching and validation.
- The `re` module and raw strings `r"..."` (prevents backslash escaping).
- **Core Metacharacters**:
  - `.` : Any single character except newline.
  - `^` : Start of string / line anchor.
  - `$` : End of string / line anchor.
  - `*` : 0 or more occurrences (greedy).
  - `+` : 1 or more occurrences (greedy).
  - `?` : 0 or 1 occurrence (optional).
  - `[abc]` : Character set (matches 'a', 'b', or 'c').
  - `[^abc]` : Negated set.
  - `{m, n}` : Quantifier range (between $m$ and $n$ times).
  - `|` : Alternation (OR).
- **Character Classes**:
  `\d` (digits `[0-9]`), `\D` (non-digits), `\w` (alphanumeric `[a-zA-Z0-9_]`), `\s` (whitespace).
- **Core Functions**:
  - `re.search(pattern, str)`: Scans entire string for first match.
  - `re.match(pattern, str)`: Matches ONLY at beginning of string.
  - `re.findall(pattern, str)`: Returns list of all matching substrings.
  - `re.finditer(pattern, str)`: Returns iterator of Match objects.
  - `re.sub(pattern, repl, str)`: Find and replace matches.
  - `re.compile(pattern)`: Compiles regex into reusable RegexObject for high throughput.

---

### 2. Database Connectivity Overview (`sqlite3`)
- Relational databases store structured records in tables with ACID guarantees.
- Python includes zero-configuration embedded database: `import sqlite3`.
- Basic workflow:
  `conn = sqlite3.connect("app.db")` -> `cursor = conn.cursor()` -> `cursor.execute("CREATE TABLE...")` -> `conn.commit()` -> `conn.close()`.
