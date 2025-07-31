# SOLID Principles in Python: Practical Examples

A practical guide to understanding and implementing the SOLID principles in Python. This repository provides clear, concise examples for each of the SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion), demonstrating how to write more maintainable, flexible, and scalable Python code. Each principle is illustrated with distinct, real-world inspired scenarios to solidify your understanding.
## Table of Contents

- [Introduction to SOLID](#introduction-to-solid)
- [Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp)
- [Open/Closed Principle (OCP)](#2-openclosed-principle-ocp)
- [Liskov Substitution Principle (LSP)](#3-liskov-substitution-principle-lsp)
- [Interface Segregation Principle (ISP)](#4-interface-segregation-principle-isp)
- [Dependency Inversion Principle (DIP)](#5-dependency-inversion-principle-dip)
- [Folder Structure](#folder-structure)
## Introduction to SOLID

Software Design is also a process to plan or convert the software requirements into a step that are needed to be carried out to develop a software system. There are several principles that are used to organize and arrange the structural components of Software design.

Here are SOLID key principles and architectural patterns along with brief explanations:

## 1. Single Responsibility Principle (SRP)

- Single Responsibility Principle (SRP): A class should have only one reason to change, meaning it should have only one responsibility or job.

- Problem: Suppose we have a User class responsible for user creation, email sending, and database persistence. A violation of the SRP would occur if the class is also responsible for storing the user in database and send email. Let's see an example without adhering to SRP: [`srp_violation.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/srp/srp_violation.py)

- Solution: We can separate the concerns into different classes, each with a single responsibility. In the refactored example, User only holds data. UserRepository is responsible for persistence, and EmailService handles email sending. Each class has one clear responsibility.Here’s a refactored example:[`srp_solution.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/srp/srp_solution.py)

## 2. Open/Closed Principle (OCP)

- Software entities (classes, modules, functions) should be open for extension but closed for modification. In other words, you should be able to add new functionality without altering the existing code.

- Problem: magine an e-commerce system that calculates discounts based on different strategies (e.g., percentage discount, fixed amount discount). If we add a new discount type (e.g., "seasonal"), we have to modify the calculate_final_price method, violating OCP.[`ocp_violation.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/ocp/ocp_violation.py)

- Solution: Now, to add a new discount, you simply create a new DiscountStrategy subclass without altering the Order class.[`ocp_solution.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/ocp/ocp_solution.py)

## 3. Liskov Substitution Principle (LSP)

- Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.In other words, a derived class should extend the functionality of the base class without changing its behavior.

- Problem: Imagine a PaymentProcessor that expects all payment methods to have a process_card_payment method. If we introduce a CashPayment method that doesn't use cards, forcing it to implement process_card_payment would be a violation (it would likely raise an error or do nothing meaningful). [`lsp_violation.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/lsp/lsp_violation.py)

- Solution: All payment methods correctly implement process_payment in a way that is specific to them, but the make_payment function can seamlessly use any PaymentMethod subclass without issues. [`lsp_solution.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/lsp/lsp_solution.py)

## 4. Interface Segregation Principle (ISP)

- A class should not be forced to implement interfaces it does not use.

- Problem: If we have a single Worker interface with methods like work_on_software_project(), drive_truck(), and attend_meetings(), and then try to make a SoftwareEngineer and a TruckDriver implement this single interface, they will be forced to implement methods they don't use (e.g., a SoftwareEngineer doesn't drive_truck). [`isp_violation.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/isp/isp_violation.py)

- Solution: By segregating the "Worker" interface into smaller, more specific interfaces (SoftwareDeveloper, Driver, MeetingParticipant), each class only implements the methods relevant to its role. [`isp_solution.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/isp/isp_solution.py)

## 5. Dependency Inversion Principle (DIP)

- High-level modules should not depend on low-level modules. Both should depend on abstractions, and abstractions should not depend on details. This principle promotes the decoupling of components in a system, making it more flexible and maintainable.

- Problem: Consider a system that sends notifications (e.g., email, SMS). The NotificationService (high-level module) directly depends on EmailSender and SMSSender (low-level modules). If we add a new notification type (e.g., push notification), we modify NotificationService. [`dip_violation.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/dip/dip_violation.py)

- Solution: NotificationService depends on the MessageSender abstraction. The specific sender (Email, SMS, Push) is injected, allowing for easy extension without modifying the NotificationService. [`dip_solution.py`](https://github.com/manas-shinde/SOLID-Principles-Python/blob/main/solid_principles/dip/dip_solution.py)

## folder structure

```code
SOLID-Principles-Python-Examples/
├── .gitignore
├── README.md
├── LICENSE
│
├── solid_principles/
│   ├── __init__.py
│   │
│   ├── srp/
│   │   ├── __init__.py
│   │   ├── srp_violation.py
│   │   ├── srp_solution.py
│   │   └── srp_explanation.md  (Optional: detailed explanation)
│   │
│   ├── ocp/
│   │   ├── __init__.py
│   │   ├── ocp_violation.py
│   │   ├── ocp_solution.py
│   │   └── ocp_explanation.md
│   │
│   ├── lsp/
│   │   ├── __init__.py
│   │   ├── lsp_violation.py
│   │   ├── lsp_solution.py
│   │   └── lsp_explanation.md
│   │
│   ├── isp/
│   │   ├── __init__.py
│   │   ├── isp_violation.py
│   │   ├── isp_solution.py
│   │   └── isp_explanation.md
│   │
│   └── dip/
│       ├── __init__.py
│       ├── dip_violation.py
│       ├── dip_solution.py
│       └── dip_explanation.md
|
└── tests/
├── __init__.py
├── test_srp.py
├── test_ocp.py
```
