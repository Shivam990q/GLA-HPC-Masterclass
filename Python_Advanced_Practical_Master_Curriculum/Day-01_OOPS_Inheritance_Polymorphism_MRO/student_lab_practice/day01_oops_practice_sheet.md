# Day 1: OOPS Practice Sheet (GLA B.Tech CSE)

## Problem 1: Enterprise Employee & Payroll Hierarchy
Build an inheritance hierarchy:
- Base class `Employee` with `name`, `emp_id`, `base_salary`.
- Subclasses `FullTimeEmployee` (adds `bonus`, calculates salary as `base_salary + bonus`) and `ContractEmployee` (has `hourly_rate`, `hours_worked`).
- Implement `@property` decorators for validation (salary cannot be negative).

## Problem 2: E-Commerce Abstract Payment Processor
- Create an Abstract Base Class `PaymentGateway` with `@abstractmethod def process_payment(self, amount: float) -> bool:`.
- Implement `RazorpayGateway`, `StripeGateway`, and `CryptoGateway` adhering to the interface.

## Problem 3: Multiple Inheritance & Diamond MRO Audit
- Implement the Diamond hierarchy: `Logger` -> `FileLogger`, `ConsoleLogger` -> `DualLogger`.
- Trace and document `DualLogger.__mro__`.
