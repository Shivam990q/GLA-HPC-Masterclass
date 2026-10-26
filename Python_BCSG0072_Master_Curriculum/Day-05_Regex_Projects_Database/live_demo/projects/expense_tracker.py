# expense_tracker.py
# Capstone Project 4: Personal Expense Tracker with Categorization & File Persistence
import os

EXPENSE_FILE = "expenses.txt"

def add_expense():
    category = input("Enter Category (Food/Travel/Study/Fun): ").strip().capitalize()
    try:
        amount = float(input("Enter Amount (INR): "))
    except ValueError:
        print("[!] Please enter a valid number!")
        return
    desc = input("Brief Description: ").strip()
    with open(EXPENSE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{category}|{amount:.2f}|{desc}\n")
    print("[+] Expense recorded successfully!")

def view_summary():
    if not os.path.exists(EXPENSE_FILE):
        print("[-] No expenses recorded yet.")
        return
    categories = {}
    total = 0.0
    with open(EXPENSE_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                cat, amt, desc = parts[0], float(parts[1]), parts[2]
                categories[cat] = categories.get(cat, 0.0) + amt
                total += amt
    print("\n=== EXPENSE SUMMARY BY CATEGORY ===")
    for cat, amt in categories.items():
        percentage = (amt / total) * 100
        print(f"  {cat:<10}: Rs. {amt:>8.2f}  ({percentage:>5.1f}%)")
    print("-" * 35)
    print(f"  TOTAL     : Rs. {total:>8.2f}")

def main():
    while True:
        print("\n--- PERSONAL EXPENSE TRACKER ---")
        print("1. Add Expense\n2. View Summary\n3. Exit")
        c = input("Choice: ").strip()
        if c == "1": add_expense()
        elif c == "2": view_summary()
        elif c == "3": break
        else: print("[!] Invalid choice")

if __name__ == "__main__":
    main()
