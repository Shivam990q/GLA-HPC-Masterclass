# Day 2 Cheatsheet: Python GUI Quick Reference

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
