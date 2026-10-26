# solution_day01_all.py
# Complete working solutions for Day 1 OOPS practice problems

from abc import ABC, abstractmethod

# Problem 1: Employee & Payroll
class Employee:
    def __init__(self, emp_id: str, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self._base_salary = base_salary

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._base_salary = value

    def calculate_total_salary(self) -> float:
        return self._base_salary

class FullTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, base_salary: float, bonus: float):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_total_salary(self) -> float:
        return self.base_salary + self.bonus

# Problem 2: Abstract Payment Processor
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"[Razorpay] Successfully routed INR {amount} through UPI/NetBanking.")
        return True

# Problem 3: Diamond MRO
class Logger:
    def log(self, msg):
        return f"[Base] {msg}"

class FileLogger(Logger):
    def log(self, msg):
        return f"[File] {super().log(msg)}"

class ConsoleLogger(Logger):
    def log(self, msg):
        return f"[Console] {super().log(msg)}"

class DualLogger(FileLogger, ConsoleLogger):
    def log(self, msg):
        return f"[Dual] {super().log(msg)}"

if __name__ == "__main__":
    ft = FullTimeEmployee("GLA001", "Aman Sharma", 65000, 15000)
    print(f"Employee {ft.name} Salary: INR {ft.calculate_total_salary()}")
    
    pay = RazorpayGateway()
    pay.process_payment(2500.0)

    dl = DualLogger()
    print("MRO Resolution:", dl.log("System startup"))
    print("MRO List:", [c.__name__ for c in DualLogger.__mro__])
