# contact_book.py
# Capstone Project 1: Smart Contact Book with Persistent File Storage
import os
import re

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name, phone, email = parts
                    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        for c in contacts.values():
            f.write(f"{c['name']}|{c['phone']}|{c['email']}\n")

def add_contact(contacts):
    name = input("Enter Contact Name: ").strip()
    phone = input("Enter 10-digit Phone: ").strip()
    if not re.match(r"^[6-9]\d{9}$", phone):
        print("[!] Invalid Indian phone number format!")
        return
    email = input("Enter Email Address: ").strip()
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        print("[!] Invalid email format!")
        return
    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
    print(f"[+] Contact '{name}' saved successfully!")

def search_contact(contacts):
    query = input("Search by Name: ").strip().lower()
    match = contacts.get(query)
    if match:
        print(f"\nFound: {match['name']} | Phone: {match['phone']} | Email: {match['email']}")
    else:
        print("[-] Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n=== SMART CONTACT BOOK ===")
        print("1. Add Contact\n2. Search Contact\n3. View All\n4. Exit")
        choice = input("Enter Choice (1-4): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            print("\n--- All Contacts ---")
            for c in contacts.values():
                print(f"Name: {c['name']:<15} | Phone: {c['phone']} | Email: {c['email']}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
