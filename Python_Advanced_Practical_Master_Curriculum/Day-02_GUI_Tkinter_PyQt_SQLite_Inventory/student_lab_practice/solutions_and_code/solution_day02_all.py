# solution_day02_all.py
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
