# desktop_inventory_system.py
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
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
