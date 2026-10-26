# Day 2: GUI Programming with Python (Tkinter, PyQt & SQLite)
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
