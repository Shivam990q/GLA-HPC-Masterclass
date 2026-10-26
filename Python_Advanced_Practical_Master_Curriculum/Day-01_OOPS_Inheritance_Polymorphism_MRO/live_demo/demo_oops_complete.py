# demo_oops_complete.py
# Full live coding demo of Classes, Encapsulation, Properties, MRO and ABC

from abc import ABC, abstractmethod

print("="*60)
print("     DEMO 1: ENCAPSULATION & VALIDATION PROPERTIES        ")
print("="*60)

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance # Private attribute

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Error: Balance cannot be negative!")
        self.__balance = value

acc = BankAccount("Shivam", 50000.0)
print(f"Account: {acc.owner} | Balance: INR {acc.balance}")
acc.balance += 15000.0
print(f"Updated Balance: INR {acc.balance}")

print("\n" + "="*60)
print("     DEMO 2: THE DIAMOND PROBLEM & C3 MRO                 ")
print("="*60)

class Device:
    def ping(self):
        return "Device"

class Scanner(Device):
    def ping(self):
        return f"Scanner -> {super().ping()}"

class Printer(Device):
    def ping(self):
        return f"Printer -> {super().ping()}"

class Copier(Scanner, Printer):
    def ping(self):
        return f"Copier -> {super().ping()}"

copier = Copier()
print("Execution Chain:", copier.ping())
print("MRO Sequence   :", [cls.__name__ for cls in Copier.__mro__])

print("\n" + "="*60)
print("     DEMO 3: ABSTRACT BASE CLASSES (ABC) & DUCK TYPING     ")
print("="*60)

class NotificationService(ABC):
    @abstractmethod
    def send_alert(self, message: str) -> bool:
        pass

class SMSNotification(NotificationService):
    def send_alert(self, message: str) -> bool:
        print(f"[SMS ALERT] Sending SMS: {message}")
        return True

class EmailNotification(NotificationService):
    def send_alert(self, message: str) -> bool:
        print(f"[EMAIL ALERT] Sending Email: {message}")
        return True

def broadcast_emergency(service: NotificationService, alert_msg: str):
    service.send_alert(alert_msg)

broadcast_emergency(SMSNotification(), "Server load exceeded 95% on Node 04")
broadcast_emergency(EmailNotification(), "Daily HPC Cluster Job Report Ready")
