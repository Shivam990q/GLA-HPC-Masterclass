"""
build_python_advanced_pptx.py
Generates 5 native widescreen (16:9) PowerPoint presentations (.pptx)
for 'Python Programming – A Practical Approach' (GLA University Advanced Curriculum).
"""

import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

PPTX_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\Python_Advanced_Practical_Master_Curriculum\Official_Presentations")
PPTX_DIR.mkdir(parents=True, exist_ok=True)

# Colors
COLOR_PRIMARY_NAVY = RGBColor(15, 23, 42)     # #0F172A
COLOR_ACCENT_BLUE   = RGBColor(37, 99, 235)    # #2563EB
COLOR_TEXT_WHITE    = RGBColor(255, 255, 255)
COLOR_TEXT_MUTED    = RGBColor(148, 163, 184)  # #94A3B8
COLOR_CARD_BG       = RGBColor(30, 41, 59)     # #1E293B

def create_deck(day_num, title, subtitle, slides_data):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- Title Slide ---
    slide = prs.slides.add_slide(blank_layout)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_PRIMARY_NAVY
    bg.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(3.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = f"GLA UNIVERSITY | ADVANCED PYTHON WORKSHOP"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_ACCENT_BLUE

    p1 = tf.add_paragraph()
    p1.text = f"Day {day_num}: {title}"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TEXT_WHITE

    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(20)
    p2.font.color.rgb = COLOR_TEXT_MUTED

    p3 = tf.add_paragraph()
    p3.text = "\nInstructor: Shivam Gupta (~SEED~) | Department of Computer Engineering & Applications"
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_ACCENT_BLUE

    # --- Content Slides ---
    for item in slides_data:
        s = prs.slides.add_slide(blank_layout)
        bg_s = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_s.fill.solid()
        bg_s.fill.fore_color.rgb = COLOR_PRIMARY_NAVY
        bg_s.line.fill.background()

        # Header
        h_box = s.shapes.add_textbox(Inches(1.0), Inches(0.6), Inches(11.333), Inches(1.0))
        h_tf = h_box.text_frame
        h_p = h_tf.paragraphs[0]
        h_p.text = item["title"]
        h_p.font.size = Pt(28)
        h_p.font.bold = True
        h_p.font.color.rgb = COLOR_TEXT_WHITE

        # Card
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.8), Inches(11.333), Inches(5.0))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_ACCENT_BLUE

        # Bullets
        c_box = s.shapes.add_textbox(Inches(1.4), Inches(2.1), Inches(10.533), Inches(4.4))
        c_tf = c_box.text_frame
        c_tf.word_wrap = True

        for b_idx, bullet in enumerate(item["bullets"]):
            bp = c_tf.paragraphs[0] if b_idx == 0 else c_tf.add_paragraph()
            bp.text = f"•  {bullet}"
            bp.font.size = Pt(18)
            bp.font.color.rgb = COLOR_TEXT_WHITE
            bp.space_after = Pt(14)

        # Presenter Notes
        if "notes" in item:
            notes_slide = s.notes_slide
            notes_tf = notes_slide.notes_text_frame
            notes_tf.text = item["notes"]

    out_file = PPTX_DIR / f"Day-0{day_num}_{title.replace(' ', '_').replace('/', '_')}.pptx"
    prs.save(out_file)
    print(f"[OK] Saved Presentation: {out_file.name}")

decks = [
    (1, "OOPS Using Python", "Classes, Encapsulation, Multiple Inheritance, MRO & Interfaces", [
        {"title": "The Python Object Model", "bullets": [
            "Everything in Python is a first-class object allocated on the heap.",
            "Classes define attributes (state) and methods (behavior).",
            "The __init__() initializer allocates instance-specific state.",
            "self provides an explicit reference to the current object instance in memory."
        ], "notes": "Emphasize that self is not a keyword in Python, but a mandatory convention."},
        {"title": "Encapsulation & Validation Properties", "bullets": [
            "Public vs Protected (_var) vs Private (__var with Name Mangling).",
            "Data hiding protects internal integrity without breaking public APIs.",
            "@property decorator transforms methods into pythonic getters.",
            "@setter decorator enforces data validation before mutation."
        ], "notes": "Show how BankAccount prevents negative balances with @balance.setter."},
        {"title": "Multiple Inheritance & The Diamond Problem", "bullets": [
            "Subclasses can inherit from multiple parent classes simultaneously.",
            "The Diamond Problem: Ambiguity when two parents override the same grandparent method.",
            "Python resolves ambiguity using the C3 Linearization Algorithm (MRO).",
            "Inspect resolution order via ClassName.__mro__ or ClassName.mro()."
        ], "notes": "Draw the Diamond graph on the whiteboard before showing the code."},
        {"title": "Polymorphism, Duck Typing & ABC Interfaces", "bullets": [
            "Polymorphism: Uniform interfaces executing specialized behaviors.",
            "Duck Typing: 'If it quacks like a duck, it is a duck.'",
            "Abstract Base Classes (abc.ABC) enforce contractual compliance.",
            "@abstractmethod raises TypeError if a subclass fails to implement required methods."
        ], "notes": "Demonstrate UPI vs Credit Card payment gateway polymorphism."}
    ]),
    (2, "GUI Programming with Python", "Event Loops, Tkinter, PyQt6, Worker Threads & SQLite CRUD", [
        {"title": "Event-Driven GUI Architecture", "bullets": [
            "Sequential CLI vs Asynchronous Event-Driven Architectures.",
            "The Event Loop (mainloop()): Listens for mouse clicks, keys, and resizes at 60 FPS.",
            "Geometry Managers in Tkinter: pack() vs grid() vs place().",
            "Why grid() is the industry standard for enterprise forms."
        ], "notes": "Contrast sequential top-down execution with infinite event loops."},
        {"title": "The Golden Rule of Multi-Threaded GUIs", "bullets": [
            "NEVER execute long-running I/O or heavy compute on the Main GUI Thread!",
            "Blocking the main thread freezes window redraws, causing OS '(Not Responding)' hangs.",
            "Offload heavy tasks to daemon background threads (threading.Thread).",
            "Communicate back to the GUI using thread-safe queues or root.after()."
        ], "notes": "Demonstrate the multi-threaded progress bar demo live."},
        {"title": "SQLite Relational Integration", "bullets": [
            "SQLite: Serverless, zero-configuration relational database stored in a single file.",
            "Python sqlite3 standard library module: connections, cursors, and transactions.",
            "CRUD Operations: Create tables, Insert records, Query with filters, Delete items.",
            "Binding SQLite query results directly to ttk.Treeview tabular tables."
        ], "notes": "Show how inventory records persist across application restarts."},
        {"title": "Capstone: Desktop Inventory System", "bullets": [
            "Full-featured GUI application with Add, Search, Delete, and Update.",
            "Live search filter querying SQLite in real time.",
            "CSV Export functionality using the csv standard library module.",
            "Packaging into a standalone executable using PyInstaller (--onefile)."
        ], "notes": "Walk through the desktop_inventory_system.py architecture."}
    ]),
    (3, "Advanced Web Development with Python", "FastAPI, Flask, REST APIs, JWT Security & WebSockets", [
        {"title": "Web Architecture: WSGI vs ASGI", "bullets": [
            "WSGI (Flask / Django): Synchronous, one thread per connection.",
            "ASGI (FastAPI / Starlette): Built on asyncio event loops, non-blocking I/O.",
            "FastAPI uses Pydantic for high-speed Rust-compiled data validation.",
            "Automatic OpenAPI / Swagger documentation generation at /docs."
        ], "notes": "Explain why FastAPI achieves 10x higher concurrency than Flask."},
        {"title": "RESTful API Design & Status Codes", "bullets": [
            "HTTP Verbs: GET (read), POST (create), PUT/PATCH (update), DELETE (remove).",
            "Status Codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found.",
            "Pydantic schemas enforce type validation and error responses automatically.",
            "Query parameters vs Path parameters vs JSON Request bodies."
        ], "notes": "Review the REST CRUD architecture implemented in the lab."},
        {"title": "Authentication & Security: JWT Flow", "bullets": [
            "Stateless authentication: Server never stores session IDs in RAM.",
            "JWT structure: Base64Url(Header) . Base64Url(Payload) . HMAC-SHA256(Signature).",
            "Password hashing using passlib / bcrypt with cryptographic salt.",
            "OAuth2 Password Bearer flow for securing sensitive endpoints."
        ], "notes": "Draw the JWT request/response lifecycle on the board."},
        {"title": "Capstone: AI Resume Screening API", "bullets": [
            "RESTful service accepting candidate resumes and job descriptions.",
            "Automated domain skill keyword extraction and semantic parsing.",
            "TF-IDF cosine similarity scoring across candidate profiles.",
            "Automated categorization: Strong Fit, Moderate Fit, Low Fit."
        ], "notes": "Run the live curl or Swagger demo on the AI resume screening endpoint."}
    ]),
    (4, "Machine Learning Pipeline Foundations", "Pandas, Feature Engineering, GridSearchCV & Model Export", [
        {"title": "The End-to-End ML Pipeline Lifecycle", "bullets": [
            "Why 80% of real-world ML projects fail: dirty data and data leakage.",
            "Data loading and exploratory analysis using Pandas and NumPy.",
            "Separation of features (X) and target labels (y).",
            "Stratified train/test splitting to preserve minority class ratios."
        ], "notes": "Emphasize that ML in production is 90% software engineering and 10% modeling."},
        {"title": "Preprocessing & Column Transformers", "bullets": [
            "Handling missing values: SimpleImputer (median for numeric, mode for categorical).",
            "Encoding categoricals: OneHotEncoder (handle_unknown='ignore').",
            "Feature scaling: StandardScaler (zero mean, unit variance).",
            "ColumnTransformer bundles disparate feature preprocessors cleanly."
        ], "notes": "Explain why test set statistics must NEVER leak into training scalers."},
        {"title": "Model Evaluation & Cross-Validation", "bullets": [
            "Why a single train/test split can produce misleading metrics.",
            "K-Fold Cross-Validation: Rotating validation across K distinct folds.",
            "Classification Metrics: Confusion Matrix, Precision, Recall, F1-Score, ROC-AUC.",
            "Choosing metrics based on business cost (e.g. False Negatives in medical/fraud)."
        ], "notes": "Show how accuracy fails on imbalanced datasets."},
        {"title": "Hyperparameter Optimization & Serialization", "bullets": [
            "GridSearchCV: Exhaustive parameter grid search across cross-validation folds.",
            "Extracting the optimal estimator via grid_search.best_estimator_.",
            "Model Serialization: Preserving trained weights and pipelines with joblib.dump().",
            "Deserializing and serving models in production with zero retraining."
        ], "notes": "Demonstrate the exported churn_pipeline_model.joblib file."}
    ]),
    (5, "Machine Learning & AI Automation", "Automated Workflows, NLP Chatbots & Production Deployment", [
        {"title": "The AI Automation Paradigm", "bullets": [
            "Bridging machine learning predictions with automated business triggers.",
            "Continuous model retraining and data drift detection.",
            "Event-driven architecture: Model outputs trigger alerts, emails, and database writes.",
            "Containerization and microservice deployment principles."
        ], "notes": "Explain how modern enterprises automate customer operations with AI."},
        {"title": "NLP Conversational Bot Architecture", "bullets": [
            "Intent Recognition: Mapping user prompts to structured business actions.",
            "TF-IDF Vectorization and Cosine Similarity matching across knowledge bases.",
            "Confidence thresholding: Routing low-confidence queries to fallback human support.",
            "Session tracking and conversation memory."
        ], "notes": "Walk through the knowledge base structure of the chatbot."},
        {"title": "Deploying AI Services with FastAPI", "bullets": [
            "Wrapping Scikit-Learn / NLP pipelines inside FastAPI endpoints.",
            "Asynchronous non-blocking inference handlers.",
            "Benchmarking throughput and latency under concurrent stress tests.",
            "Deploying on Uvicorn with multi-worker process management."
        ], "notes": "Demonstrate locust / curl stress testing against the chatbot API."},
        {"title": "Course Capstone: AI Customer Support Bot", "bullets": [
            "Full working conversational bot answering GLA University inquiries.",
            "Intents: Admissions, Hostel Facilities, Placement Records, and HPC Labs.",
            "Sub-10ms response latency on CPU inference.",
            "Production-ready REST API architecture ready for deployment."
        ], "notes": "Celebrate the completion of the 5-day Advanced Python Workshop."}
    ])
]

for d_num, title, sub, slides in decks:
    create_deck(d_num, title, sub, slides)

print("[SUCCESS] All 5 Advanced Python Presentations (.pptx) Generated Successfully!")
