# Day 1: Object-Oriented Programming (OOP) in Python
## Comprehensive Lecture & Whiteboard Guide

---

### 1. Fundamental OOP Concepts & Philosophy
Python is a multi-paradigm language, but its object model is ubiquitous: **everything in Python is an object**, including functions, classes, and primitive types (`int`, `str`).

#### Classes vs Instances:
- **Class (`class`)**: The blueprint/template defining attributes (state) and methods (behavior).
- **Instance**: A concrete realization of the class allocated in memory (`obj = MyClass()`).
- **`__init__(self, ...)`**: The constructor/initializer called immediately after object creation (`__new__`).
- **`self`**: A reference to the current instance of the class passed implicitly as the first argument to instance methods.

```python
class Student:
    # Class Attribute (Shared across all instances in memory)
    university_name = "GLA University"
    total_students = 0

    def __init__(self, name: str, roll_no: int, marks: float):
        # Instance Attributes (Unique per instance)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        Student.total_students += 1

    def display_details(self) -> str:
        return f"Roll: {self.roll_no} | Name: {self.name} | Marks: {self.marks} | Uni: {self.university_name}"
```

---

### 2. Encapsulation & Data Hiding
Encapsulation bundles data (attributes) and methods that operate on that data within a class while restricting direct access to internal representation.

#### Python Access Specifier Conventions:
1. **Public**: `self.name` (Accessible everywhere).
2. **Protected**: `self._balance` (Single underscore convention: intended for internal class and subclass use only).
3. **Private**: `self.__pin` (Double underscore: triggers **Name Mangling** to `_ClassName__pin` to prevent accidental overriding).

#### Property Decorators (`@property`, `@setter`, `@deleter`):
Provides pythonic getters and setters with validation without breaking public API ergonomics.

```python
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        self.account_holder = account_holder
        self.__balance = initial_balance # Private attribute

    @property
    def balance(self) -> float:
        """Getter for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount: float):
        """Setter with validation logic"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
```

---

### 3. Inheritance & Method Overriding
Inheritance enables a child class (subclass) to inherit attributes and methods from a parent class (base class).

- **`super()`**: Returns a proxy object delegating method calls to a parent or sibling class.
- **Method Overriding**: Redefining a parent class method in the subclass to provide specialized behavior.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hello, I am {self.name}, age {self.age}."

class Professor(Person):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department

    def introduce(self) -> str:
        # Extending parent method
        base_msg = super().introduce()
        return f"{base_msg} I teach in the {self.department} department."
```

---

### 4. Multiple Inheritance & Method Resolution Order (MRO)
Python supports multiple inheritance, where a class can inherit from more than one parent.

#### The Diamond Problem:
```
       A
      / \
     B   C
      \ /
       D
```
When class `D` inherits from both `B` and `C`, and both override a method from `A`, which method does `D` execute?
Python resolves this deterministically using the **C3 Linearization Algorithm (MRO)**:
- View MRO via `D.__mro__` or `D.mro()`.
- Rule: Subclasses before parent classes; left-to-right order of base classes in definition.

```python
class A:
    def greet(self):
        return "Greeting from A"

class B(A):
    def greet(self):
        return "Greeting from B -> " + super().greet()

class C(A):
    def greet(self):
        return "Greeting from C -> " + super().greet()

class D(B, C):
    def greet(self):
        return "Greeting from D -> " + super().greet()

# MRO of D: [D, B, C, A, object]
# Output: Greeting from D -> Greeting from B -> Greeting from C -> Greeting from A
```

---

### 5. Polymorphism, Duck Typing & Abstract Interfaces
- **Polymorphism**: The ability of different classes to respond to the same method call with distinct implementations.
- **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."* Python doesn't check explicit inheritance; it checks whether the requested method exists.
- **Abstract Base Classes (`abc.ABC`)**: Enforces contract enforcement at instantiation time using `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class UPIPayment(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing UPI payment of INR {amount}")
        return True

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing Credit Card payment of INR {amount}")
        return True
```
