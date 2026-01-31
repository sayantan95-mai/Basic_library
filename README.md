# Library Management System

## Overview
This is a Python-based Library Management System designed to demonstrate core Object-Oriented Programming (OOP) concepts. The application allows users to manage library items like books and DVDs, with data automatically saved to a local JSON file.

## Key Features
* **Object-Oriented Design**: Implements **Inheritance** (Books/DVDs inheriting from a generic Item), **Polymorphism** (custom behavior for different item types), and **Encapsulation** (protected data attributes).
* **Data Persistence**: Automatically saves and loads library records using `library_data.json`.
* **Duplicate Prevention**: Checks for existing IDs before adding new items.
* **Modular Architecture**: Separates logic (`src`), data handling (`data`), and execution (`main.py`).

## Project Structure
```text
LibrarySystem/
├── main.py                 # Entry point for the application
├── README.md               # Project documentation
├── src/
│   ├── __init__.py
│   ├── items.py            # Classes: LibraryItem, Book, DVD
│   └── users.py            # (Future) Member management logic
└── data/
    ├── __init__.py
    ├── data.py             # Handles JSON file operations (Save/Load)
    └── library_data.json   # Database file