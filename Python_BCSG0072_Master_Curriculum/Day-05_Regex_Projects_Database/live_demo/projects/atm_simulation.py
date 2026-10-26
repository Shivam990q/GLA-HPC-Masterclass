# atm_simulation.py
# Capstone Project 6: ATM Banking Simulation using Functions & Custom Exceptions

class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass

class InvalidPINError(Exception):
    """Raised when wrong PIN is entered."""
    pass

accounts = {
    "1001": {"name": "Aarav Sharma", "pin": "1234", "balance": 15000.0}
}

def verify_pin(acc_num, entered_pin):
    acc = accounts.get(acc_num)
    if not acc or acc["pin"] != entered_pin:
        raise InvalidPINError("Incorrect Account Number or PIN!")
    return acc

def withdraw(acc, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive!")
    if amount > acc["balance"]:
        raise InsufficientBalanceError(f"Insufficient funds! Available balance: Rs. {acc['balance']:.2f}")
    acc["balance"] -= amount
    print(f"[+] Please collect Rs. {amount:.2f}. Remaining Balance: Rs. {acc['balance']:.2f}")

def deposit(acc, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive!")
    acc["balance"] += amount
    print(f"[+] Deposited Rs. {amount:.2f}. New Balance: Rs. {acc['balance']:.2f}")

def main():
    print("=== SECURE ATM BANKING SIMULATION ===")
    acc_no = input("Enter Account Number: ").strip()
    pin = input("Enter 4-digit PIN: ").strip()
    
    try:
        current_acc = verify_pin(acc_no, pin)
        print(f"\nWelcome {current_acc['name']}!")
        while True:
            print("\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Exit")
            ch = input("Select: ").strip()
            if ch == "1":
                print(f"[i] Balance: Rs. {current_acc['balance']:.2f}")
            elif ch == "2":
                amt = float(input("Amount to withdraw: "))
                withdraw(current_acc, amt)
            elif ch == "3":
                amt = float(input("Amount to deposit: "))
                deposit(current_acc, amt)
            elif ch == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("[!] Invalid option")
    except (InvalidPINError, InsufficientBalanceError, ValueError) as e:
        print(f"[ERROR] Transaction Failed: {e}")

if __name__ == "__main__":
    main()
