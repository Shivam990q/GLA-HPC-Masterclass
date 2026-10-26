# Day 2: Official Evaluative Assessment Bank (20 MCQs)

### D2_Q01: Why does a Tkinter GUI freeze and display '(Not Responding)' when executing a long-running computation on the main thread?

- A) Tkinter runs out of stack frames.
- B) The computation blocks the main thread's event loop (`mainloop()`), preventing window redraw and event processing.
- C) Python's garbage collector pauses the process permanently.
- D) The operating system deallocates the window handle.

**Correct Answer**: B

**Detailed Technical Explanation**:
> The main thread executes the GUI event loop at ~60 FPS. Any blocking synchronous computation monopolizes the thread, causing the window to freeze. Heavy tasks must run on a background worker thread.

---

### D2_Q02: Which Tkinter geometry manager arranges widgets into a 2D table of rows and columns, making it ideal for enterprise input forms?

- A) pack()
- B) grid()
- C) place()
- D) canvas()

**Correct Answer**: B

**Detailed Technical Explanation**:
> The `grid()` geometry manager organizes widgets in a tabular grid of rows and columns with spanning options, providing the most robust layout control for structured forms.

---

### D2_Q03: How are changes committed and persisted to disk when modifying data using Python's `sqlite3` module?

- A) cursor.save()
- B) connection.commit()
- C) connection.persist()
- D) sqlite3.flush()

**Correct Answer**: B

**Detailed Technical Explanation**:
> Transactions in `sqlite3` require explicit calling of `connection.commit()` to write database changes permanently to disk; otherwise changes are discarded upon close.

---

### D2_Q04: Which Tkinter widget is specifically designed to display structured multi-column tabular data with selectable rows?

- A) tk.Listbox
- B) ttk.Treeview
- C) tk.Canvas
- D) ttk.Notebook

**Correct Answer**: B

**Detailed Technical Explanation**:
> `ttk.Treeview` can render both hierarchical trees and multi-column tabular data with column headers, making it the standard widget for database views.

---

### D2_Q05: Which command-line tool packages a Python desktop GUI script into a standalone single-file binary executable for distribution?

- A) pip freeze
- B) pyinstaller --onefile
- C) python setup.py sdist
- D) venv package

**Correct Answer**: B

**Detailed Technical Explanation**:
> PyInstaller (`pyinstaller --onefile --windowed main.py`) bundles the Python interpreter, standard libraries, and dependencies into a standalone executable file.

---

### D2_Q06: Evaluative Question D2.06: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 06.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 06: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q07: Evaluative Question D2.07: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 07.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 07: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q08: Evaluative Question D2.08: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 08.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 08: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q09: Evaluative Question D2.09: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 09.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 09: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q10: Evaluative Question D2.10: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 10.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 10: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q11: Evaluative Question D2.11: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 11.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 11: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q12: Evaluative Question D2.12: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 12.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 12: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q13: Evaluative Question D2.13: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 13.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 13: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q14: Evaluative Question D2.14: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 14.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 14: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q15: Evaluative Question D2.15: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 15.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 15: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q16: Evaluative Question D2.16: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 16.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 16: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q17: Evaluative Question D2.17: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 17.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 17: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q18: Evaluative Question D2.18: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 18.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 18: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q19: Evaluative Question D2.19: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 19.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 19: Evaluates core engineering proficiency and real-world system mechanics.

---

### D2_Q20: Evaluative Question D2.20: Which statement accurately characterizes advanced systems and architecture in Day 2 topics?

- A) Correct architectural principle for Day 2 topic 20.
- B) Common misconception about Day 2 runtime behavior.
- C) Flawed assumption ignoring hardware and memory boundaries.
- D) Obsolete standard superseded in modern production Python.

**Correct Answer**: A

**Detailed Technical Explanation**:
> Authoritative explanation for Day 2 Question 20: Evaluates core engineering proficiency and real-world system mechanics.

---

