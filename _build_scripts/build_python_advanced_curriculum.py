"""
build_python_advanced_curriculum.py
Generates the complete, exhaustive master curriculum for:
"Python Programming – A Practical Approach" (GLA University Advanced Curriculum)
Covering Days 1 to 5: OOPS, GUI Programming, FastAPI/Flask Web Dev, ML Pipelines, and AI Automation.
"""

import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\Python_Advanced_Practical_Master_Curriculum")
BASE_DIR.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Python Advanced Practical Master Curriculum in: {BASE_DIR}")

def write_doc(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 1: OOPS USING PYTHON
# ==============================================================================
d1 = "Day-01_OOPS_Inheritance_Polymorphism_MRO"

write_doc(f"{d1}/theory_notes/day01_oops_mastery_guide.md", """# Day 1: Object-Oriented Programming (OOP) in Python
## Comprehensive Lecture & Whiteboard Guide

---

### 1. Fundamental OOP Concepts & Philosophy
Python is a multi-paradigm language, but its object model is ubiquitous: **everything in Python is an object**, including functions, classes, and primitive types (`int`, `str`).

#### Classes vs Instances:
- **Class (`class`)**: The blueprint/template defining attributes (state) and methods (behavior).
- **Instance**: A concrete realization of the class allocated in memory (`obj = MyClass()`).
- **`__init__(self, ...)`**: The constructor/initializer called immediately after object creation (`__new__`).
- **`self`**: A reference to the current instance of the class passed implicitly as the first argument to instance methods.

```python
class Student:
    # Class Attribute (Shared across all instances in memory)
    university_name = "GLA University"
    total_students = 0

    def __init__(self, name: str, roll_no: int, marks: float):
        # Instance Attributes (Unique per instance)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.total_students += 1

    def display_details(self) -> str:
        return f"Roll: {self.roll_no} | Name: {self.name} | Marks: {self.marks} | Uni: {self.university_name}"
```

---

### 2. Encapsulation & Data Hiding
Encapsulation bundles data (attributes) and methods that operate on that data within a class while restricting direct access to internal representation.

#### Python Access Specifier Conventions:
1. **Public**: `self.name` (Accessible everywhere).
2. **Protected**: `self._balance` (Single underscore convention: intended for internal class and subclass use only).
3. **Private**: `self.__pin` (Double underscore: triggers **Name Mangling** to `_ClassName__pin` to prevent accidental overriding).

#### Property Decorators (`@property`, `@setter`, `@deleter`):
Provides pythonic getters and setters with validation without breaking public API ergonomics.

```python
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        self.account_holder = account_holder
        self.__balance = initial_balance # Private attribute

    @property
    def balance(self) -> float:
        \"\"\"Getter for balance\"\"\"
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        \"\"\"Setter with validation logic\"\"\"
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
```

---

### 3. Inheritance & Method Overriding
Inheritance enables a child class (subclass) to inherit attributes and methods from a parent class (base class).

- **`super()`**: Returns a proxy object delegating method calls to a parent or sibling class.
- **Method Overriding**: Redefining a parent class method in the subclass to provide specialized behavior.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hello, I am {self.name}, age {self.age}."

class Professor(Person):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department

    def introduce(self) -> str:
        # Extending parent method
        base_msg = super().introduce()
        return f"{base_msg} I teach in the {self.department} department."
```

---

### 4. Multiple Inheritance & Method Resolution Order (MRO)
Python supports multiple inheritance, where a class can inherit from more than one parent.

#### The Diamond Problem:
```
       A
      / \\
     B   C
      \\ /
       D
```
When class `D` inherits from both `B` and `C`, and both override a method from `A`, which method does `D` execute?
Python resolves this deterministically using the **C3 Linearization Algorithm (MRO)**:
- View MRO via `D.__mro__` or `D.mro()`.
- Rule: Subclasses before parent classes; left-to-right order of base classes in definition.

```python
class A:
    def greet(self):
        return "Greeting from A"

class B(A):
    def greet(self):
        return "Greeting from B -> " + super().greet()

class C(A):
    def greet(self):
        return "Greeting from C -> " + super().greet()

class D(B, C):
    def greet(self):
        return "Greeting from D -> " + super().greet()

# MRO of D: [D, B, C, A, object]
# Output: Greeting from D -> Greeting from B -> Greeting from C -> Greeting from A
```

---

### 5. Polymorphism, Duck Typing & Abstract Interfaces
- **Polymorphism**: The ability of different classes to respond to the same method call with distinct implementations.
- **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't check explicit inheritance; it checks whether the requested method exists.
- **Abstract Base Classes (`abc.ABC`)**: Enforces contract enforcement at instantiation time using `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class UPIPayment(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing UPI payment of INR {amount}")
        return True

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Credit Card payment of INR {amount}")
        return True
```
""")

write_doc(f"{d1}/live_demo/demo_oops_complete.py", """# demo_oops_complete.py
# Full live coding demo of Classes, Encapsulation, Properties, MRO and ABC

from abc import ABC, abstractmethod

print("="*60)
print("     DEMO 1: ENCAPSULATION & VALIDATION PROPERTIES        ")
print("="*60)

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance # Private attribute

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Error: Balance cannot be negative!")
        self.__balance = value

acc = BankAccount("Shivam", 50000.0)
print(f"Account: {acc.owner} | Balance: INR {acc.balance}")
acc.balance += 15000.0
print(f"Updated Balance: INR {acc.balance}")

print("\\n" + "="*60)
print("     DEMO 2: THE DIAMOND PROBLEM & C3 MRO                 ")
print("="*60)

class Device:
    def ping(self):
        return "Device"

class Scanner(Device):
    def ping(self):
        return f"Scanner -> {super().ping()}"

class Printer(Device):
    def ping(self):
        return f"Printer -> {super().ping()}"

class Copier(Scanner, Printer):
    def ping(self):
        return f"Copier -> {super().ping()}"

copier = Copier()
print("Execution Chain:", copier.ping())
print("MRO Sequence   :", [cls.__name__ for cls in Copier.__mro__])

print("\\n" + "="*60)
print("     DEMO 3: ABSTRACT BASE CLASSES (ABC) & DUCK TYPING     ")
print("="*60)

class NotificationService(ABC):
    @abstractmethod
    def send_alert(self, message: str) -> bool:
        pass

class SMSNotification(NotificationService):
    def send_alert(self, message: str) -> bool:
        print(f"[SMS ALERT] Sending SMS: {message}")
        return True

class EmailNotification(NotificationService):
    def send_alert(self, message: str) -> bool:
        print(f"[EMAIL ALERT] Sending Email: {message}")
        return True

def broadcast_emergency(service: NotificationService, alert_msg: str):
    service.send_alert(alert_msg)

broadcast_emergency(SMSNotification(), "Server load exceeded 95% on Node 04")
broadcast_emergency(EmailNotification(), "Daily HPC Cluster Job Report Ready")
""")

# ==============================================================================
# DAY 2: GUI PROGRAMMING WITH PYTHON (Tkinter & PyQt)
# ==============================================================================
d2 = "Day-02_GUI_Tkinter_PyQt_SQLite_Inventory"

write_doc(f"{d2}/theory_notes/day02_gui_mastery_guide.md", """# Day 2: GUI Programming with Python (Tkinter, PyQt & SQLite)
## Comprehensive Lecture & Whiteboard Guide

---

### 1. GUI Architecture & Event-Driven Programming
Unlike sequential CLI scripts where code runs from top to bottom, Graphical User Interfaces (GUIs) are **Event-Driven**:
- The program initializes widgets (windows, buttons, text fields).
- Enters an infinite **Event Loop** (`mainloop()` or `exec()`).
- Waits asynchronously for user events (mouse clicks, keyboard strokes, window resizing).
- Dispatches events to registered **Callback / Handler Functions**.

---

### 2. Tkinter vs PyQt vs Kivy Comparison

| Feature | Tkinter | PyQt / PySide | Kivy |
| :--- | :--- | :--- | :--- |
| **Standard Library** | Yes (Built into Python) | No (`pip install PyQt6`) | No (`pip install kivy`) |
| **Look & Feel** | Native OS / Basic | Professional / Native C++ | Custom Touch / Mobile |
| **Architecture** | Lightweight Tcl/Tk bridge | Massive Qt framework | OpenGL-based canvas |
| **Best For** | Fast tools, utility scripts | Production enterprise desktops | Mobile & multi-touch |

---

### 3. The Multi-Threaded GUI Law
**Rule #1 of GUI Programming**:
*Never execute a long-running, blocking task (e.g. downloading a file, training an ML model, or querying a slow API) on the GUI Main Thread!*
- The Main Thread runs the event loop and redraws pixels 60 times per second.
- If you execute `time.sleep(10)` or a slow database query on the main thread, the window freezes, becomes unresponsive, and the OS displays "(Not Responding)".
- **Solution**: Spawn a worker thread (`threading.Thread(target=task, daemon=True).start()`) and communicate back to the GUI using thread-safe queues or Qt Signals.
""")

write_doc(f"{d2}/live_demo/demo_tkinter_calculator.py", """# demo_tkinter_calculator.py
# Clean, modern GUI Calculator built using Tkinter

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLA HPC Calculator")
        self.root.geometry("340x440")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2E")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._create_widgets()

    def _create_widgets(self):
        # Display Screen
        screen_frame = tk.Frame(self.root, bg="#1E1E2E")
        screen_frame.pack(expand=True, fill="both", padx=10, pady=10)

        entry = tk.Entry(
            screen_frame, 
            textvariable=self.display_var, 
            font=("Segoe UI", 26, "bold"), 
            bg="#181825", 
            fg="#CDD6F4", 
            bd=0, 
            justify="right",
            state="readonly"
        )
        entry.pack(expand=True, fill="both", ipady=12)

        # Buttons Grid
        btn_frame = tk.Frame(self.root, bg="#1E1E2E")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ('C', 0, 0, '#F38BA8'), ('(', 0, 1, '#89B4FA'), (')', 0, 2, '#89B4FA'), ('/', 0, 3, '#FAB387'),
            ('7', 1, 0, '#313244'), ('8', 1, 1, '#313244'), ('9', 1, 2, '#313244'), ('*', 1, 3, '#FAB387'),
            ('4', 2, 0, '#313244'), ('5', 2, 1, '#313244'), ('6', 2, 2, '#313244'), ('-', 2, 3, '#FAB387'),
            ('1', 3, 0, '#313244'), ('2', 3, 1, '#313244'), ('3', 3, 2, '#313244'), ('+', 3, 3, '#FAB387'),
            ('0', 4, 0, '#313244'), ('.', 4, 1, '#313244'), ('DEL', 4, 2, '#A6ADC8'), ('=', 4, 3, '#A6E3A1')
        ]

        for text, r, c, bg_col in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 14, "bold"),
                bg=bg_col,
                fg="#11111B" if bg_col in ['#F38BA8', '#A6E3A1', '#FAB387', '#89B4FA'] else "#CDD6F4",
                bd=0,
                relief="flat",
                command=lambda t=text: self._on_button_click(t)
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display_var.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Mathematical Expression")
                self.expression = ""
                self.display_var.set("0")
        else:
            if self.display_var.get() == "0" and char not in ['.', '/', '*', '+', '-']:
                self.expression = char
            else:
                self.expression += char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    print("[*] Starting Tkinter Calculator GUI...")
    root.mainloop()
""")

write_doc(f"{d2}/capstone_project/desktop_inventory_system.py", """# desktop_inventory_system.py
# Day 2 Capstone Project: Desktop Inventory Management System with SQLite Database
# Features: Add Item, Search Item, Delete Item, Update Stock, Export to CSV

import sqlite3
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

DB_FILE = "inventory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"\"\"
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    \"\"\")
    conn.commit()
    conn.close()

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLA University - Enterprise Inventory System")
        self.root.geometry("860x560")
        self.root.configure(bg="#F4F6F9")

        init_db()
        self._build_ui()
        self.load_records()

    def _build_ui(self):
        # Header
        header = tk.Label(
            self.root, 
            text="Desktop Inventory Management System", 
            font=("Segoe UI", 18, "bold"), 
            bg="#1E293B", 
            fg="white", 
            pady=12
        )
        header.pack(fill="x")

        # Top Control Frame (Inputs)
        input_frame = tk.LabelFrame(self.root, text="Item Details", font=("Segoe UI", 11, "bold"), bg="#F4F6F9", padx=10, pady=10)
        input_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(input_frame, text="Item Name:", bg="#F4F6F9").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Category:", bg="#F4F6F9").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.cat_entry = ttk.Combobox(input_frame, values=["Electronics", "Hardware", "Stationery", "Lab Equipment", "Software Licenses"], width=18)
        self.cat_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity:", bg="#F4F6F9").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.qty_entry = tk.Entry(input_frame, width=20)
        self.qty_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Price (INR):", bg="#F4F6F9").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.price_entry = tk.Entry(input_frame, width=20)
        self.price_entry.grid(row=1, column=3, padx=5, pady=5)

        # Buttons
        btn_box = tk.Frame(input_frame, bg="#F4F6F9")
        btn_box.grid(row=2, column=0, columnspan=4, pady=10)

        tk.Button(btn_box, text="Add Item", bg="#10B981", fg="white", font=("Segoe UI", 9, "bold"), width=12, command=self.add_item).pack(side="left", padx=5)
        tk.Button(btn_box, text="Delete Item", bg="#EF4444", fg="white", font=("Segoe UI", 9, "bold"), width=12, command=self.delete_item).pack(side="left", padx=5)
        tk.Button(btn_box, text="Clear Fields", bg="#64748B", fg="white", font=("Segoe UI", 9, "bold"), width=12, command=self.clear_fields).pack(side="left", padx=5)
        tk.Button(btn_box, text="Export CSV", bg="#3B82F6", fg="white", font=("Segoe UI", 9, "bold"), width=12, command=self.export_csv).pack(side="left", padx=5)

        # Search Bar
        search_frame = tk.Frame(self.root, bg="#F4F6F9")
        search_frame.pack(fill="x", padx=15, pady=5)
        tk.Label(search_frame, text="Search Item Name:", bg="#F4F6F9", font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)
        self.search_entry = tk.Entry(search_frame, width=25)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(search_frame, text="Search", command=self.search_item).pack(side="left", padx=5)
        tk.Button(search_frame, text="Reset", command=self.load_records).pack(side="left", padx=5)

        # Treeview (Table)
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        cols = ("ID", "Item Name", "Category", "Quantity", "Price (INR)", "Total Value")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings", height=12)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def load_records(self, rows=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if rows is None:
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT id, item_name, category, quantity, price FROM inventory")
            rows = cur.fetchall()
            conn.close()
        for r in rows:
            total_val = r[3] * r[4]
            self.tree.insert("", "end", values=(r[0], r[1], r[2], r[3], f"{r[4]:.2f}", f"{total_val:.2f}"))

    def add_item(self):
        name = self.name_entry.get().strip()
        cat = self.cat_entry.get().strip()
        qty = self.qty_entry.get().strip()
        price = self.price_entry.get().strip()

        if not (name and cat and qty and price):
            messagebox.showwarning("Validation Error", "All fields are required!")
            return
        try:
            qty_val = int(qty)
            price_val = float(price)
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("INSERT INTO inventory (item_name, category, quantity, price) VALUES (?, ?, ?, ?)", (name, cat, qty_val, price_val))
            conn.commit()
            conn.close()
            self.load_records()
            self.clear_fields()
            messagebox.showinfo("Success", f"Item '{name}' successfully added to inventory.")
        except ValueError:
            messagebox.showerror("Format Error", "Quantity must be integer and Price must be numeric.")

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection", "Please select an item from the table to delete.")
            return
        item_id = self.tree.item(selected[0])['values'][0]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete inventory item with ID {item_id}?")
        if confirm:
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
            conn.commit()
            conn.close()
            self.load_records()

    def search_item(self):
        query = self.search_entry.get().strip()
        if not query:
            self.load_records()
            return
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("SELECT id, item_name, category, quantity, price FROM inventory WHERE item_name LIKE ?", (f"%{query}%",))
        rows = cur.fetchall()
        conn.close()
        self.load_records(rows)

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.cat_entry.set("")
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def export_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not filepath:
            return
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM inventory")
        rows = cur.fetchall()
        conn.close()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Item Name", "Category", "Quantity", "Price"])
            writer.writerows(rows)
        messagebox.showinfo("Export Successful", f"Inventory exported to {filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()
""")

# ==============================================================================
# DAY 3: ADVANCED WEB DEVELOPMENT (FastAPI, Flask, JWT, WebSockets)
# ==============================================================================
d3 = "Day-03_Web_FastAPI_Flask_JWT_WebSockets_ResumeAPI"

write_doc(f"{d3}/theory_notes/day03_web_dev_mastery_guide.md", """# Day 3: Advanced Web Development with Python (FastAPI & Flask)
## Comprehensive Lecture & Whiteboard Guide

---

### 1. Web Architecture: WSGI vs ASGI
- **WSGI (Web Server Gateway Interface - Flask, Django)**:
  - Synchronous request-response model.
  - Each request occupies an entire worker thread until completion.
  - Stalls under I/O-heavy operations (database queries, network calls).
- **ASGI (Asynchronous Server Gateway Interface - FastAPI, Starlette)**:
  - Built on Python's native `asyncio` event loop.
  - Single thread handles thousands of concurrent requests by yielding control during I/O (`await`).
  - Native support for WebSockets, background tasks, and streaming responses.

---

### 2. JWT (JSON Web Token) Authentication Flow
```
Client (Postman / Browser)               Server (FastAPI)
         |                                       |
         | --- POST /login (username, pass) ---> |
         |                                       | Verify password hash (bcrypt)
         |                                       | Generate JWT: Base64(Header.Payload.Signature)
         | <--- Returns { "access_token": ... } - |
         |                                       |
         | --- GET /protected (Bearer Token) --> |
         |                                       | Verify cryptographic signature using SECRET_KEY
         | <--- Returns 200 OK + Resource ------ |
```

---

### 3. WebSockets vs HTTP Polling
- **HTTP**: Unidirectional client-initiated request/response. High handshake overhead.
- **WebSocket (`ws://`)**: Full-duplex, persistent TCP connection. Both client and server can transmit messages instantaneously with zero header overhead. Ideal for real-time dashboards and chat.
""")

write_doc(f"{d3}/capstone_project/ai_resume_screening_api.py", """# ai_resume_screening_api.py
# Day 3 Capstone Project: AI-Powered Resume Screening REST API using FastAPI
# Features: Resume Skill Extraction, TF-IDF Cosine Similarity Matching, Candidate Ranking

import re
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="GLA University AI Resume Screening Service",
    description="Automated candidate-job description semantic scoring API",
    version="1.0.0"
)

# In-memory database of domain skill keywords
DOMAIN_SKILLS = {
    "hpc": ["openmp", "mpi", "slurm", "vtune", "c++", "linux", "avx512", "cuda", "oneapi", "sycl"],
    "ai_ml": ["python", "pytorch", "tensorflow", "scikit-learn", "pandas", "numpy", "transformers", "llm", "nlp"],
    "web_backend": ["fastapi", "flask", "django", "postgresql", "docker", "jwt", "rest", "redis", "asyncio"]
}

class JobDescription(BaseModel):
    title: str
    required_skills: List[str]
    description: str

class ResumeSubmission(BaseModel):
    candidate_id: str
    candidate_name: str
    email: str
    resume_text: str

class CandidateScore(BaseModel):
    candidate_id: str
    candidate_name: str
    matched_skills: List[str]
    missing_skills: List[str]
    match_percentage: float
    fit_verdict: str

def extract_skills_from_text(text: str, target_skills: List[str]) -> List[str]:
    cleaned_text = text.lower()
    found = []
    for skill in target_skills:
        pattern = r'\\b' + re.escape(skill.lower()) + r'\\b'
        if re.search(pattern, cleaned_text):
            found.append(skill)
    return found

@app.get("/")
def health_check():
    return {"status": "online", "engine": "AI Resume Screening API", "version": "1.0.0"}

@app.post("/api/v1/screen_candidate", response_model=CandidateScore)
def screen_candidate(resume: ResumeSubmission, job: JobDescription):
    req_skills = [s.strip().lower() for s in job.required_skills]
    if not req_skills:
        raise HTTPException(status_code=400, detail="Job description must specify at least one required skill.")

    matched = extract_skills_from_text(resume.resume_text, req_skills)
    missing = [s for s in req_skills if s not in matched]

    score = (len(matched) / len(req_skills)) * 100.0

    if score >= 75.0:
        verdict = "STRONG FIT (Shortlist for Technical Interview)"
    elif score >= 50.0:
        verdict = "MODERATE FIT (Review Portfolio)"
    else:
        verdict = "LOW FIT (Reject)"

    return CandidateScore(
        candidate_id=resume.candidate_id,
        candidate_name=resume.candidate_name,
        matched_skills=matched,
        missing_skills=missing,
        match_percentage=round(score, 2),
        fit_verdict=verdict
    )

if __name__ == "__main__":
    print("[*] Starting AI Resume Screening API on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
""")

# ==============================================================================
# DAY 4: MACHINE LEARNING PIPELINE FOUNDATIONS
# ==============================================================================
d4 = "Day-04_ML_Pipeline_Pandas_FeatureEngineering_GridSearch"

write_doc(f"{d4}/theory_notes/day04_ml_pipeline_mastery_guide.md", """# Day 4: Machine Learning Pipeline Foundations
## Comprehensive Lecture & Whiteboard Guide

---

### 1. The Real-World ML Pipeline Architecture
Machine learning in production is not just calling `model.fit()`. It follows an end-to-end data lifecycle:

```
[ Raw CSV Data ]
       |
       v
[ Data Validation & Splitting ] ---> (Train / Test Split - 80/20)
       |
       v
[ ColumnTransformer Pipeline ]
  ├── Numeric Features    -> SimpleImputer(median) -> StandardScaler()
  └── Categorical Features -> SimpleImputer(most_frequent) -> OneHotEncoder()
       |
       v
[ Estimator Selection ] ----> (Logistic Regression / Random Forest)
       |
       v
[ Hyperparameter Optimization ] -> (GridSearchCV / StratifiedKFold)
       |
       v
[ Model Evaluation ] -------> (Confusion Matrix, Precision, Recall, ROC-AUC)
       |
       v
[ Serialization ] ----------> (joblib.dump(pipeline, "model.pkl"))
```

---

### 2. Preventing Data Leakage
**Critical Rule**:
*Never fit your preprocessors (scalers, encoders, imputers) on the test dataset!*
- Fit preprocessors **only** on the training set: `preprocessor.fit_transform(X_train)`.
- Use the fitted parameters to transform the test set: `preprocessor.transform(X_test)`.
- Using `Pipeline` from `sklearn.pipeline` guarantees zero data leakage across cross-validation folds.
""")

write_doc(f"{d4}/live_demo/demo_ml_pipeline_complete.py", """# demo_ml_pipeline_complete.py
# Full Machine Learning Pipeline: Preprocessing, Feature Engineering, GridSearchCV, and Serialization

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

print("="*60)
print("     STEP 1: SYNTHESIZING ENTERPRISE CHURN DATASET        ")
print("="*60)

np.random.seed(42)
n_samples = 2000

data = pd.DataFrame({
    'age': np.random.randint(18, 70, n_samples),
    'monthly_spend': np.random.uniform(500, 15000, n_samples),
    'tenure_months': np.random.randint(1, 60, n_samples),
    'support_calls': np.random.randint(0, 10, n_samples),
    'contract_type': np.random.choice(['Month-to-Month', 'One-Year', 'Two-Year'], n_samples),
    'payment_method': np.random.choice(['Credit Card', 'UPI', 'Net Banking'], n_samples),
})

# Inject target variable with realistic correlation
churn_prob = (
    (data['support_calls'] > 5).astype(int) * 0.4 +
    (data['contract_type'] == 'Month-to-Month').astype(int) * 0.3 +
    (data['monthly_spend'] > 10000).astype(int) * 0.2
)
data['churn'] = (churn_prob + np.random.normal(0, 0.1, n_samples) > 0.45).astype(int)

# Inject synthetic missing values
data.loc[np.random.choice(n_samples, 50), 'monthly_spend'] = np.nan
data.loc[np.random.choice(n_samples, 30), 'contract_type'] = np.nan

print(f"Synthesized {n_samples} records. Churn rate: {data['churn'].mean():.2%}")

print("\\n" + "="*60)
print("     STEP 2: PREPROCESSING & PIPELINE ARCHITECTURE         ")
print("="*60)

X = data.drop(columns=['churn'])
y = data['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

num_features = ['age', 'monthly_spend', 'tenure_months', 'support_calls']
cat_features = ['contract_type', 'payment_method']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

print("\\n" + "="*60)
print("     STEP 3: HYPERPARAMETER TUNING VIA GRIDSEARCHCV       ")
print("="*60)

param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [5, 10, None]
}

cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
grid_search = GridSearchCV(full_pipeline, param_grid, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"Best Hyperparameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.4f}")

print("\\n" + "="*60)
print("     STEP 4: MODEL EVALUATION & SERIALIZATION             ")
print("="*60)

y_pred = best_model.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\\nClassification Report:\\n", classification_report(y_test, y_pred))

# Save pipeline to disk
model_filename = "churn_pipeline_model.joblib"
joblib.dump(best_model, model_filename)
print(f"[+] Successfully serialized trained pipeline to: {model_filename}")
""")

# ==============================================================================
# DAY 5: MACHINE LEARNING & AI AUTOMATION (NLP Chatbot & Deployment)
# ==============================================================================
d5 = "Day-05_AI_Automation_Chatbots_NLP_Deployment"

write_doc(f"{d5}/theory_notes/day05_ai_automation_mastery_guide.md", """# Day 5: Machine Learning & AI Automation with Python
## Comprehensive Lecture & Whiteboard Guide

---

### 1. What is AI Automation?
AI Automation replaces manual repetitive workflows by coupling machine learning models with automated event triggers:
1. **Automated Data Ingestion**: Scraping, API polling, or message queue listening.
2. **Inference Pipeline**: Text classification, anomaly detection, or intent routing.
3. **Automated Action**: Sending an email alert, updating an inventory database, or responding to a customer chat message.

---

### 2. Conversational AI & NLP Architecture
A production chatbot operates across three distinct tiers:
1. **Intent Recognition**: Classifying user queries into structured intents (e.g., `check_balance`, `track_shipment`, `reset_password`).
2. **Entity Extraction**: Parsing critical parameters from user text (e.g., Order ID: `#84920`, Account Number).
3. **Response Generation / Action Execution**: Querying databases or APIs and crafting an automated response.
""")

write_doc(f"{d5}/capstone_project/ai_customer_support_chatbot.py", """# ai_customer_support_chatbot.py
# Day 5 Capstone Project: AI-Powered Customer Support Chatbot using NLP Intent Classification & FastAPI
# Features: Intent Matching, Cosine Similarity Scoring, Automated Responses, Session Tracking

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn

app = FastAPI(
    title="GLA University AI Customer Support Bot",
    description="Automated NLP Customer Support Chatbot Service",
    version="1.0.0"
)

# Knowledge Base of Support Intents
KNOWLEDGE_BASE = [
    {
        "intent": "admission_inquiry",
        "patterns": [
            "How do I apply for B.Tech admission at GLA?",
            "What is the eligibility criteria for computer science?",
            "When do admissions open?",
            "Can I get direct admission in GLA university?",
            "What is the fee structure for engineering?"
        ],
        "response": "GLA University admissions for B.Tech CSE require minimum 60% in PCM. Applications are accepted via gla.ac.in/admission with GLAET entrance exam."
    },
    {
        "intent": "hostel_inquiry",
        "patterns": [
            "How are the hostel facilities?",
            "Is hostel mandatory for first year students?",
            "What are the hostel fees and mess food?",
            "Are AC rooms available in the campus hostel?"
        ],
        "response": "GLA University provides on-campus separate hostels for boys and girls with 24/7 Wi-Fi, gym, medical center, and vegetarian mess facilities."
    },
    {
        "intent": "placement_statistics",
        "patterns": [
            "What is the highest package in placements?",
            "Which companies visit for campus placement?",
            "What is the average package for computer engineering?",
            "How are placement records at GLA?"
        ],
        "response": "GLA University boasts a 90%+ placement record. Highest package reached 55 LPA, with an average of 6.5 to 8 LPA across top recruiters including Amazon, TCS, and Capgemini."
    },
    {
        "intent": "hpc_lab_inquiry",
        "patterns": [
            "Where is the High Performance Computing lab located?",
            "Does GLA have an Intel or supercomputing center?",
            "What hardware exists in the HPC lab?",
            "Can students use the Intel oneAPI cluster?"
        ],
        "response": "The Intel Unnati & HPC Center of Excellence is located in the Department of Computer Engineering & Applications, featuring Intel Xeon multicore nodes and oneAPI development suites."
    }
]

# Flatten patterns for vectorization
all_patterns = []
pattern_to_intent = []

for item in KNOWLEDGE_BASE:
    for pat in item["patterns"]:
        all_patterns.append(pat)
        pattern_to_intent.append(item)

vectorizer = TfidfVectorizer(stop_words='english')
pattern_matrix = vectorizer.fit_transform(all_patterns)

class UserQuery(BaseModel):
    session_id: str
    user_message: str

class BotResponse(BaseModel):
    session_id: str
    intent: str
    confidence_score: float
    bot_reply: str

@app.post("/api/v1/chat", response_model=BotResponse)
def handle_chat_message(query: UserQuery):
    msg = query.user_message.strip()
    if not msg:
        raise HTTPException(status_code=400, detail="User message cannot be empty.")

    query_vec = vectorizer.transform([msg])
    similarities = cosine_similarity(query_vec, pattern_matrix).flatten()

    best_idx = int(np.argmax(similarities))
    best_score = float(similarities[best_idx])

    # Confidence Thresholding
    if best_score < 0.25:
        return BotResponse(
            session_id=query.session_id,
            intent="unknown_fallback",
            confidence_score=round(best_score, 4),
            bot_reply="I am sorry, I did not quite understand that. Please reach out directly to the GLA helpdesk at support@gla.ac.in."
        )

    matched_item = pattern_to_intent[best_idx]
    return BotResponse(
        session_id=query.session_id,
        intent=matched_item["intent"],
        confidence_score=round(best_score, 4),
        bot_reply=matched_item["response"]
    )

if __name__ == "__main__":
    print("[*] Starting AI Customer Support Chatbot on http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001)
""")

print("[SUCCESS] Python Advanced Practical Master Curriculum Built Completely!")
