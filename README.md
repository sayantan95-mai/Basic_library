# Library Management System

## Overview
This project is a modular Library Management System built in Python. It is designed to demonstrate key **Object-Oriented Programming (OOP)** concepts such as Inheritance, Polymorphism, and Encapsulation. The system allows librarians to manage an inventory of Books, DVDs, and Magazines, as well as track Members and their borrowed items.

## Key Features
* **Multi-Type Inventory**: Manage different item types (Books, DVDs, Magazines) with unique attributes (Pages, Runtime, Issue Date).
* **Borrowing System**: Tracks who has borrowed what. Prevents users from borrowing items that are already out.
* **Smart Returns & Fines**: automatically calculates overdue fines based on the item type:
    * **Books**: 21 days loan, $0.50/day fine.
    * **DVDs**: 7 days loan, $2.00/day fine.
    * **Magazines**: 7 days loan, $1.00/day fine.
* **Data Persistence**: All data (items and users) is saved to JSON files (`library_data.json`, `users.json`) so nothing is lost when the program closes.
* **Menu Interface**: Easy-to-use command line menu powered by Python's `match-case` statement.

## Project Structure
```text
LibrarySystem/
├── main.py                 # The main entry point (Menu & Logic)
├── README.md               # Project documentation
├── src/
│   ├── __init__.py
│   ├── items.py            # Classes: LibraryItem, Book, DVD, Magazine
│   └── users.py            # Classes: Member
└── data/
    ├── __init__.py
    ├── data.py             # Handles JSON file operations (Save/Load)
    ├── library_data.json   # Storage for inventory
    └── users.json          # Storage for member records