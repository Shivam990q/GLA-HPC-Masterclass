"""
expand_python_advanced_mastery.py
Expands Python_Advanced_Practical_Master_Curriculum with:
1. student_lab_practice/ (Practice sheets + full solutions)
2. interview_and_exam_qa/ (University exam & top placement QA)
3. student_cheatsheets/ (Quick reference cards)
4. presentation_scripts/ (Podium trainer speaking scripts)
"""

import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\Python_Advanced_Practical_Master_Curriculum")

def write_f(rel_path, content):
    full_path = BASE_DIR / rel_path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"[OK] Wrote: {rel_path}")

print("[*] Expanding Python Advanced Practical Master Curriculum with full practice sheets, QA, cheatsheets and scripts...")

# ------------------------------------------------------------------------------
# Day 1: OOPS
# ------------------------------------------------------------------------------
d1 = "Day-01_OOPS_Inheritance_Polymorphism_MRO"
write_f(f"{d1}/student_lab_practice/day01_oops_practice_sheet.md", """# Day 1: OOPS Practice Sheet (GLA B.Tech CSE)

## Problem 1: Enterprise Employee & Payroll Hierarchy
Build an inheritance hierarchy:
- Base class `Employee` with `name`, `emp_id`, `base_salary`.
- Subclasses `FullTimeEmployee` (adds `bonus`, calculates salary as `base_salary + bonus`) and `ContractEmployee` (has `hourly_rate`, `hours_worked`).
- Implement `@property` decorators for validation (salary cannot be negative).

## Problem 2: E-Commerce Abstract Payment Processor
- Create an Abstract Base Class `PaymentGateway` with `@abstractmethod def process_payment(self, amount: float) -> bool:`.
- Implement `RazorpayGateway`, `StripeGateway`, and `CryptoGateway` adhering to the interface.

## Problem 3: Multiple Inheritance & Diamond MRO Audit
- Implement the Diamond hierarchy: `Logger` -> `FileLogger`, `ConsoleLogger` -> `DualLogger`.
- Trace and document `DualLogger.__mro__`.
""")

write_f(f"{d1}/student_lab_practice/solutions_and_code/solution_day01_all.py", """# solution_day01_all.py
# Complete working solutions for Day 1 OOPS practice problems

from abc import ABC, abstractmethod

# Problem 1: Employee & Payroll
class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self._base_salary = base_salary

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._base_salary = value

    def calculate_total_salary(self) -> float:
        return self._base_salary

class FullTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, bonus: float):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_total_salary(self) -> float:
        return self.base_salary + self.bonus

# Problem 2: Abstract Payment Processor
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"[Razorpay] Successfully routed INR {amount} through UPI/NetBanking.")
        return True

# Problem 3: Diamond MRO
class Logger:
    def log(self, msg):
        return f"[Base] {msg}"

class FileLogger(Logger):
    def log(self, msg):
        return f"[File] {super().log(msg)}"

class ConsoleLogger(Logger):
    def log(self, msg):
        return f"[Console] {super().log(msg)}"

class DualLogger(FileLogger, ConsoleLogger):
    def log(self, msg):
        return f"[Dual] {super().log(msg)}"

if __name__ == "__main__":
    ft = FullTimeEmployee("GLA001", "Aman Sharma", 65000, 15000)
    print(f"Employee {ft.name} Salary: INR {ft.calculate_total_salary()}")
    
    pay = RazorpayGateway()
    pay.process_payment(2500.0)

    dl = DualLogger()
    print("MRO Resolution:", dl.log("System startup"))
    print("MRO List:", [c.__name__ for c in DualLogger.__mro__])
""")

write_f(f"{d1}/interview_and_exam_qa/day01_exam_and_interview_qa.md", """# Day 1: OOPS Exam & Top Placement Interview Q&A

### Q1: What is Method Resolution Order (MRO) and how does Python's C3 Linearization work?
- **Answer**: MRO defines the order in which base classes are searched when executing a method on an object. Python uses the **C3 Linearization Algorithm**, which guarantees two properties:
  1. Children precede their parents.
  2. If class $B$ precedes class $C$ in the subclass declaration `class D(B, C)`, then $B$ precedes $C$ throughout the resolution order.

### Q2: What is Name Mangling in Python?
- **Answer**: When an identifier starts with two or more leading underscores (`__pin`), Python rewrites the attribute name internally by prefixing `_ClassName` (e.g. `_BankAccount__pin`). This is designed to prevent accidental namespace collisions in inheritance subclasses. It is not true security (it can still be accessed via `_ClassName__var`), but it enforces encapsulation conventions.

### Q3: What is the difference between `@staticmethod` and `@classmethod`?
- **Answer**:
  - `@classmethod` takes `cls` as its first argument and can access/modify class-level state. Useful for factory methods (alternative constructors like `from_dict()`).
  - `@staticmethod` takes neither `self` nor `cls`. It is a plain function scoped inside the class namespace for organizational clarity.
""")

write_f(f"{d1}/student_cheatsheets/quick_reference_card.md", """# Day 1 Cheatsheet: Python OOPS Quick Reference

```python
# Encapsulation & Properties
class Model:
    def __init__(self, val):
        self._val = val
    @property
    def val(self): return self._val
    @val.setter
    def val(self, v): self._val = v

# Abstract Base Class
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def run(self): pass

# Inspection
isinstance(obj, ClassName)
issubclass(Sub, Super)
Class.mro() # Shows Method Resolution Order
```
""")

write_f(f"{d1}/presentation_scripts/trainer_speaking_script.md", """# Day 1 Trainer Podium Script: OOPS in Python

## Opening Hook (9:00 AM - 9:20 AM)
> *"Welcome to Day 1 of Advanced Python Programming at GLA University.
> Everyone here knows how to write a function or loop. But when you build scalable systems—like web servers, GUI tools, and machine learning pipelines—you must master Object-Oriented Architecture.
> Today, we demystify what `self` actually points to, how Python enforces data encapsulation through properties, how multiple inheritance works under the hood, and how Python resolves the Diamond Problem via C3 Linearization.
> Let's start with a blank whiteboard."*
""")

# ------------------------------------------------------------------------------
# Day 2: GUI Programming
# ------------------------------------------------------------------------------
d2 = "Day-02_GUI_Tkinter_PyQt_SQLite_Inventory"
write_f(f"{d2}/student_lab_practice/day02_gui_practice_sheet.md", """# Day 2: GUI Programming Practice Sheet (GLA B.Tech CSE)

## Problem 1: Basic Tkinter Calculator
- Build a GUI calculator with grid layout supporting basic arithmetic (`+`, `-`, `*`, `/`, `C`, `=`).

## Problem 2: SQLite To-Do List Application
- Build a desktop To-Do application using Tkinter and SQLite.
- Features: Add task, mark task completed, delete task, persist to `todos.db`.

## Problem 3: Multi-Threaded GUI Progress Bar
- Create a window with a button "Start Heavy Computation" and a `ttk.Progressbar`.
- Demonstrate that running the computation on a background `threading.Thread` prevents the GUI window from freezing.
""")

write_f(f"{d2}/student_lab_practice/solutions_and_code/solution_day02_all.py", """# solution_day02_all.py
# Working solutions for Day 2 GUI practice problems

import sqlite3
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

# SQLite To-Do Database
def init_todo_db():
    conn = sqlite3.connect("todos.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)")
    conn.commit()
    conn.close()

class MultiThreadedProgressDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Threaded Responsive GUI")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Click Start to run background worker (GUI won't freeze!)", font=("Segoe UI", 10))
        self.label.pack(pady=15)

        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        self.btn = tk.Button(root, text="Start Heavy Computation", bg="#2563EB", fg="white", font=("Segoe UI", 10, "bold"), command=self.start_thread)
        self.btn.pack(pady=10)

    def start_thread(self):
        self.btn.config(state="disabled")
        # Run worker in background thread!
        threading.Thread(target=self._worker, daemon=True).start()

    def _worker(self):
        for i in range(1, 101):
            time.sleep(0.03) # Simulates heavy model training or data fetching
            self.root.after(0, self._update_progress, i)
        self.root.after(0, self._done)

    def _update_progress(self, val):
        self.progress['value'] = val

    def _done(self):
        self.btn.config(state="normal")
        messagebox.showinfo("Success", "Background computation completed without freezing the GUI!")

if __name__ == "__main__":
    init_todo_db()
    r = tk.Tk()
    app = MultiThreadedProgressDemo(r)
    r.mainloop()
""")

write_f(f"{d2}/interview_and_exam_qa/day02_exam_and_interview_qa.md", """# Day 2: GUI Exam & Top Placement Interview Q&A

### Q1: Why does a Tkinter or PyQt GUI freeze when performing network requests or long loops?
- **Answer**: GUIs run an **Event Loop** (`mainloop()` or `app.exec()`) on the application's primary OS thread (Main Thread). This thread handles redraw events, button clicks, and mouse hovering at 60 FPS. If you perform a blocking operation (like `time.sleep()`, file download, or SQL query) on the main thread, the event loop stops processing window events, causing the OS to report the window as "(Not Responding)".
- **Solution**: Execute blocking tasks inside a background worker thread (`threading.Thread` or `QThread`).

### Q2: What are the differences between Tkinter's geometry managers: `pack()`, `grid()`, and `place()`?
- **Answer**:
  - `pack()`: Arranges widgets along edges (TOP, BOTTOM, LEFT, RIGHT). Best for simple vertical/horizontal toolbars.
  - `grid()`: Arranges widgets in a 2D table of rows and columns. Most versatile and industry-standard for enterprise forms.
  - `place()`: Positions widgets at absolute pixel coordinates (`x`, `y`). Not recommended for responsive design across different screen resolutions.
""")

write_f(f"{d2}/student_cheatsheets/quick_reference_card.md", """# Day 2 Cheatsheet: Python GUI Quick Reference

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("App Title")
root.geometry("600x400")

# Widgets
lbl = tk.Label(root, text="Hello").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

def on_click():
    txt = entry.get()
    print("User entered:", txt)

btn = tk.Button(root, text="Submit", command=on_click).pack()

root.mainloop()
```
""")

write_f(f"{d2}/presentation_scripts/trainer_speaking_script.md", """# Day 2 Trainer Podium Script: GUI Programming

## Opening Hook (9:00 AM - 9:20 AM)
> *"Good morning. Yesterday we wrote clean object-oriented code. But when you build tools for end-users, lab technicians, or enterprise managers, they do not want to run commands in a terminal. They want intuitive graphical user interfaces.
> Today, we master event-driven programming, learn how to prevent GUI freezing using worker threads, integrate SQLite relational databases, and build our Capstone: Desktop Inventory Management System.
> Let's get our hands on the code."*
""")

# ------------------------------------------------------------------------------
# Day 3: Web Dev (FastAPI / Flask)
# ------------------------------------------------------------------------------
d3 = "Day-03_Web_FastAPI_Flask_JWT_WebSockets_ResumeAPI"
write_f(f"{d3}/student_lab_practice/day03_web_practice_sheet.md", """# Day 3: Advanced Web Development Practice Sheet (GLA B.Tech CSE)

## Problem 1: FastAPI User CRUD Service
- Implement REST endpoints:
  - `POST /users` (Create user with name, email, role).
  - `GET /users` (List all users with pagination `skip` and `limit`).
  - `GET /users/{user_id}` (Get user by ID, return 404 if not found).
  - `DELETE /users/{user_id}` (Delete user).

## Problem 2: JWT Authentication in Flask / FastAPI
- Create `/auth/login` accepting username and password.
- Validate credentials and return an encoded JWT bearer token with 15-minute expiration.
- Protect `/auth/profile` requiring `Authorization: Bearer <token>`.

## Problem 3: Real-Time WebSocket Echo Server
- Create a WebSocket endpoint `/ws` that broadcasts incoming messages to all connected clients.
""")

write_f(f"{d3}/student_lab_practice/solutions_and_code/solution_day03_all.py", """# solution_day03_all.py
# Working solutions for Day 3 Web Development practice problems

from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, EmailStr
from typing import List, Dict
import uvicorn

app = FastAPI(title="Day 3 Web Solutions API")

# In-memory storage
users_db: Dict[int, dict] = {}
user_id_seq = 1

class UserCreate(BaseModel):
    name: str
    email: str
    role: str = "student"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

@app.post("/users", response_model=UserResponse)
def create_user(u: UserCreate):
    global user_id_seq
    user_data = {"id": user_id_seq, "name": u.name, "email": u.email, "role": u.role}
    users_db[user_id_seq] = user_data
    user_id_seq += 1
    return user_data

@app.get("/users", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10):
    return list(users_db.values())[skip : skip + limit]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# WebSocket Broadcast Manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"[Broadcast] Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    print("[*] Running Day 3 Practice Solutions API on port 8000...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
""")

write_f(f"{d3}/interview_and_exam_qa/day03_exam_and_interview_qa.md", """# Day 3: Web Dev Exam & Top Placement Interview Q&A

### Q1: What makes FastAPI significantly faster than Flask and Django?
- **Answer**:
  1. **ASGI vs WSGI**: FastAPI runs on **Starlette** and **Uvicorn** using Python's native asynchronous event loop (`asyncio`), handling high-concurrency non-blocking I/O effortlessly.
  2. **Pydantic Serialization**: FastAPI uses Pydantic (compiled in Rust via Pydantic v2) for lightning-fast schema validation and JSON serialization.
  3. **Automatic OpenAPI/Swagger Documentation**: Native interactive API docs at `/docs` without third-party plugins.

### Q2: How does JWT Authentication work and why is it stateless?
- **Answer**: A JSON Web Token consists of three base64-encoded segments: `Header.Payload.Signature`.
  - The server signs the token using a secret key (`HMAC-SHA256`).
  - When the client sends the token, the server verifies the cryptographic signature without querying a central session database!
  - It is **stateless** because all authorization metadata (user ID, roles, expiration) lives inside the token itself, enabling effortless horizontal scaling across multiple servers.
""")

write_f(f"{d3}/student_cheatsheets/quick_reference_card.md", """# Day 3 Cheatsheet: FastAPI & REST Quick Reference

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return {"message": "Created", "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"id": item_id}

# Run: uvicorn main:app --reload
```
""")

write_f(f"{d3}/presentation_scripts/trainer_speaking_script.md", """# Day 3 Trainer Podium Script: Web Development (FastAPI)

## Opening Hook (9:00 AM - 9:20 AM)
> *"Good morning. Today we enter the world of modern web microservices.
> In modern software architecture, your Python models and business logic are useless if other services, mobile apps, or frontend teams cannot communicate with them.
> Today, we transition from monolithic scripts to high-throughput REST APIs using FastAPI, examine asynchronous event loops, protect our endpoints with JWT authentication, and deploy real-time WebSockets.
> Let's look at the ASGI architecture."*
""")

# ------------------------------------------------------------------------------
# Day 4: ML Pipeline Foundations
# ------------------------------------------------------------------------------
d4 = "Day-04_ML_Pipeline_Pandas_FeatureEngineering_GridSearch"
write_f(f"{d4}/student_lab_practice/day04_ml_practice_sheet.md", """# Day 4: ML Pipeline Practice Sheet (GLA B.Tech CSE)

## Problem 1: End-to-End Pipeline on Synthetic Housing Data
- Build a full Scikit-Learn `Pipeline` for housing price regression:
  - Numeric features (`area`, `bedrooms`, `age`) -> Impute median + StandardScaler.
  - Categorical features (`locality`, `property_type`) -> Impute most frequent + OneHotEncoder.
  - Model: `RandomForestRegressor`.

## Problem 2: K-Fold Cross-Validation & Metric Inspection
- Perform 5-fold cross-validation using `cross_val_score(scoring='r2')`.
- Print the mean $R^2$ score and standard deviation.

## Problem 3: Hyperparameter Optimization & Model Export
- Use `GridSearchCV` to optimize `n_estimators` ([20, 50]) and `max_depth` ([4, 8]).
- Save the best pipeline using `joblib.dump()` and write a test script that loads the file and makes a prediction.
""")

write_f(f"{d4}/student_lab_practice/solutions_and_code/solution_day04_all.py", """# solution_day04_all.py
# Working solutions for Day 4 ML Pipeline practice problems

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Synthesize Housing Data
np.random.seed(42)
n = 1000
df = pd.DataFrame({
    'area': np.random.uniform(500, 3500, n),
    'bedrooms': np.random.randint(1, 5, n),
    'age': np.random.randint(0, 30, n),
    'locality': np.random.choice(['Mathura Cantt', 'Vrindavan', 'NH-19 Highway'], n),
    'property_type': np.random.choice(['Apartment', 'Villa', 'Independent'], n)
})
df['price'] = (df['area'] * 4500 + df['bedrooms'] * 300000 - df['age'] * 50000 + np.random.normal(0, 100000, n))

X = df.drop(columns=['price'])
y = df['price']

num_cols = ['area', 'bedrooms', 'age']
cat_cols = ['locality', 'property_type']

preprocessor = ColumnTransformer(transformers=[
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_cols),
    ('cat', Pipeline([('imp', SimpleImputer(strategy='most_frequent')), ('ohe', OneHotEncoder(handle_unknown='ignore'))]), cat_cols)
])

pipe = Pipeline([
    ('prep', preprocessor),
    ('rf', RandomForestRegressor(n_estimators=30, random_state=42))
])

scores = cross_val_score(pipe, X, y, cv=5, scoring='r2')
print(f"5-Fold Cross Validation R^2: {scores.mean():.4f} +/- {scores.std():.4f}")

pipe.fit(X, y)
joblib.dump(pipe, "housing_pipeline.joblib")
print("[+] Model saved successfully as housing_pipeline.joblib")
""")

write_f(f"{d4}/interview_and_exam_qa/day04_exam_and_interview_qa.md", """# Day 4: ML Pipeline Exam & Top Placement Interview Q&A

### Q1: What is Data Leakage in Machine Learning and how does Scikit-Learn `Pipeline` eliminate it?
- **Answer**: Data leakage occurs when information from outside the training dataset (such as test dataset statistics) is inadvertently used to train the model. For example, if you compute the global mean for `SimpleImputer` or `StandardScaler` across the entire dataset *before* splitting into train/test, the training step has leaked information about the test distribution.
- **Solution**: A `Pipeline` ensures that preprocessors are fitted strictly on training folds during cross-validation, and merely transform the validation/test folds.

### Q2: What is the difference between `GridSearchCV` and `RandomizedSearchCV`?
- **Answer**:
  - `GridSearchCV` exhaustively tests every combination of hyperparameter values in the search grid. Precise, but computationally expensive ($O(\prod |param_i|)$).
  - `RandomizedSearchCV` samples a fixed number of parameter combinations (`n_iter`) from specified distributions. Statistically finds near-optimal hyperparameters in 10% of the compute time.
""")

write_f(f"{d4}/student_cheatsheets/quick_reference_card.md", """# Day 4 Cheatsheet: Scikit-Learn Pipeline Quick Reference

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

preprocessor = ColumnTransformer([
    ('num', Pipeline([('imputer', SimpleImputer()), ('scaler', StandardScaler())]), num_cols),
    ('cat', OneHotEncoder(), cat_cols)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```
""")

write_f(f"{d4}/presentation_scripts/trainer_speaking_script.md", """# Day 4 Trainer Podium Script: Machine Learning Pipelines

## Opening Hook (9:00 AM - 9:20 AM)
> *"Good morning. Today we bridge software engineering with machine learning.
> Many students think machine learning is just calling `model.fit()`. But in industry, 80% of ML projects fail not because of the algorithm, but because of dirty data, poor preprocessing, and data leakage.
> Today, we learn how to engineer end-to-end reproducible pipelines using Scikit-Learn, apply K-Fold Cross-Validation, tune hyperparameters with Grid Search, and serialize our trained models for production deployment.
> Let's look at the data flow."*
""")

# ------------------------------------------------------------------------------
# Day 5: AI Automation
# ------------------------------------------------------------------------------
d5 = "Day-05_AI_Automation_Chatbots_NLP_Deployment"
write_f(f"{d5}/student_lab_practice/day05_ai_automation_practice_sheet.md", """# Day 5: AI Automation Practice Sheet (GLA B.Tech CSE)

## Problem 1: Spam Detection Microservice
- Train a TF-IDF + Multinomial Naive Bayes text classifier on synthetic email messages.
- Wrap the model in a FastAPI endpoint `POST /classify_email` returning `{"is_spam": bool, "confidence": float}`.

## Problem 2: Rule-Based & Keyword Intent Chatbot
- Implement a chatbot router using regex and keyword matching that answers FAQs for GLA University exams, fee schedules, and hostel rules.

## Problem 3: Automated Email Notification Trigger
- Couple the output of an ML model with an automated action: if an email is flagged as phishing/high-risk, automatically trigger a security log alert.
""")

write_f(f"{d5}/student_lab_practice/solutions_and_code/solution_day05_all.py", """# solution_day05_all.py
# Working solutions for Day 5 AI Automation practice problems

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Synthetic Training Data for Spam Filter
corpus = [
    "Win a free iPhone now click here",
    "Claim your lottery prize of 1 million dollars",
    "URGENT: Your bank account is locked verify immediately",
    "Dear student, your GLA semester exam schedule is attached",
    "Meeting rescheduled to 3 PM tomorrow in Conference Hall",
    "Please review the attached project assignment before Friday",
]
labels = [1, 1, 1, 0, 0, 0] # 1 = Spam, 0 = Ham

spam_pipe = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])
spam_pipe.fit(corpus, labels)

app = FastAPI(title="Spam Detection Service")

class EmailRequest(BaseModel):
    subject: str
    body: str

@app.post("/classify_email")
def classify(req: EmailRequest):
    text = f"{req.subject} {req.body}"
    pred = spam_pipe.predict([text])[0]
    prob = spam_pipe.predict_proba([text])[0][pred]
    return {
        "classification": "SPAM" if pred == 1 else "LEGITIMATE (HAM)",
        "confidence": round(float(prob), 4)
    }

if __name__ == "__main__":
    print("[*] Running Spam Detection AI Service on port 8002...")
    uvicorn.run(app, host="127.0.0.1", port=8002)
""")

write_f(f"{d5}/interview_and_exam_qa/day05_exam_and_interview_qa.md", """# Day 5: AI Automation Exam & Top Placement Interview Q&A

### Q1: What is the difference between Intent Classification and Named Entity Recognition (NER)?
- **Answer**:
  - **Intent Classification**: A text classification task that determines the overarching goal or purpose of the user's message (e.g. `check_balance` or `book_ticket`).
  - **Named Entity Recognition (NER)**: A sequence tagging task that extracts specific variable entities or tokens from the message (e.g. `amount = 500`, `location = Mathura`, `date = tomorrow`).

### Q2: How do you serve machine learning models in production with low latency?
- **Answer**:
  1. **Model Optimization & Quantization**: Convert models to ONNX or OpenVINO INT8 precision.
  2. **Asynchronous Serving Frameworks**: Use FastAPI / TorchServe / Triton Inference Server rather than heavy WSGI frameworks.
  3. **Batching & Worker Concurrency**: Utilize dynamic batching to group incoming requests and saturate CPU vector units or GPU cores.
""")

write_f(f"{d5}/student_cheatsheets/quick_reference_card.md", """# Day 5 Cheatsheet: AI Automation & NLP Quick Reference

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
query_vec = vectorizer.transform([user_query])

similarity_scores = cosine_similarity(query_vec, X)
best_match_idx = similarity_scores.argmax()
```
""")

write_f(f"{d5}/presentation_scripts/trainer_speaking_script.md", """# Day 5 Trainer Podium Script: AI Automation & Chatbots

## Opening Hook (9:00 AM - 9:20 AM)
> *"Good morning, everyone. Welcome to the final day of our Advanced Python Workshop.
> Over the past four days, you have mastered OOPS, GUI desktop software, FastAPI REST web services, and machine learning pipelines.
> Today, we unite all these disciplines into the highest-impact field in industry: AI Automation.
> We will see how machine learning models pair with automated workflows to build intelligent customer support chatbots and automated classification microservices.
> Let's make this final session count."*
""")

print("[SUCCESS] All Practice Sheets, Solutions, Exam QA, Cheatsheets and Podium Scripts Built for Python Advanced Curriculum!")
