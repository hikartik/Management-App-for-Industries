# FusionOps: Unified Industrial Operations Platform

**FusionOps** is a comprehensive DBMS solution that provides a unified platform for managing various operations within a product-based company. It integrates modules for authentication, management, sales, finance, production, and HR—enabling seamless, secure, and efficient company operations.

---

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Database Design](#database-design)
- [User Interface](#user-interface)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Challenges & Future Enhancements](#challenges--future-enhancements)
- [License](#license)
- [Contact](#contact)

---

## Introduction
FusionOps streamlines industrial operations by unifying critical departmental processes in a single system. Designed as a DBMS project, it enhances decision-making, improves efficiency, and ensures data security for all company operations.

---

## Key Features
- **Unified Management:** Centralizes authentication, managerial tasks, sales, finance, production, and HR operations.
- **Robust Database Design:** Efficiently stores and manages company data with a well-structured MySQL schema.
- **User-Friendly Interface:** Built with HTML, CSS, JavaScript, and Bootstrap for intuitive interaction.
- **Security Focused:** Implements authentication, authorization, data encryption, and regular security audits.
- **Scalable & Performant:** Optimized for high performance and future scalability with efficient database queries and modular architecture.

---

## System Architecture
The system is composed of the following modules:
- **Authentication Module:** Manages secure user login.
- **Manager Module:** Provides comprehensive company data and management tools.
- **Sales Department Module:** Handles customer information and sales data.
- **Finance Department Module:** Manages financial transactions, budgeting, and reporting.
- **Production Department Module:** Oversees production processes and inventory management.
- **HR Department Module:** Manages employee records, recruitment, and payroll.

---

## Database Design
The database schema includes:
- **Customers Table:** CustomerID, CustomerName, ContactNumber, Email, Address.
- **Employees Table:** EmployeeID, FirstName, LastName, DateOfBirth, Gender, Department, Position, Salary, Password, Email.
- **Orders Table:** OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalAmount.
- **Products Table:** ProductID, ProductName, Category, QuantityInStock, UnitPrice, ReorderLevel.
- **Suppliers Table:** SupplierID, SupplierName, ContactNumber, Email, Address.
- **Transactions Table:** TransactionID, TransactionDate, ProductID, TransactionType, Quantity, Remarks.

---

## User Interface
The UI is designed with modern web technologies:
- **Frontend:** HTML, CSS, JavaScript, and Bootstrap for responsive design.
- **Screenshots & Diagrams:** Detailed visuals are provided in the project documentation to illustrate UI elements and workflows.

---

## Setup & Installation
1. **Install XAMPP:**  
   Download and install [XAMPP](https://www.apachefriends.org/index.html) to set up your local server.

2. **Database Creation:**  
   Create the MySQL database using the provided schema.

3. **Project Initialization:**  
   Open your terminal and run the following command to start the project:
   ```bash
   python main.py
