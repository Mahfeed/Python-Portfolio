```markdown
![Python](https://img.shields.io/badge/Python-Expertise%20in%20Progress-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Actively%20Learning-28A745?style=for-the-badge)
![Goal](https://img.shields.io/badge/Goal-Python%20Automation%20%26%20Freelancing-FF6F00?style=for-the-badge)

# 🐍 Python Automation Journey

**Mastering Python for Automation, Data Cleaning, and Freelancing Projects** — building production-ready tools through consistent daily practice.

---

## 📅 Learning Log

| Date       | Milestone                          |
|------------|------------------------------------|
| Mar 4, 2026 | Environment setup & Greeting Program |
| Mar 5, 2026 | Grade Calculator with validation   |
| Mar 6, 2026 | Number Guessing Game               |
| Mar 7, 2026 | Task Manager CLI                   |
| Mar 8, 2026 | Inventory Tracker CLI (Dictionaries) |

---

## 🚀 Project Roadmap

| Session | Topic                        | Status          | Project                  |
|---------|------------------------------|-----------------|--------------------------|
| **01**  | Environment Setup & Basics   | ✅ Complete     | Greeting Program         |
| **02**  | Conditions & Logic Flow      | ✅ Complete     | Grade Calculator         |
| **03**  | Loops & Iteration            | ✅ Complete     | Number Guessing Game     |
| **04**  | Lists & CLI Programs         | ✅ Complete     | Task Manager             |
| **05**  | Dictionaries & Data Structures | ✅ Complete   | Inventory Tracker        |
| **06**  | File Handling                | ⏳ Upcoming     | CSV Data Cleaner         |
| **07**  | Automation Scripts           | ⏳ Upcoming     | Excel + Python Pipeline  |

---

## 📊 Learning Progress

```markdown
Python Fundamentals     ██████████ 95%
Automation Skills       ████░░░░░░ 40%
Data Cleaning           ██░░░░░░░░ 25%
Freelancing Ready       █░░░░░░░░░ 10%
```

---

## 🌟 Session Highlights

### Session 01 — Environment Setup & Basics
**Date:** March 4, 2026  
**Focus:** Toolchain configuration and core syntax

**Accomplishments**
- Installed and configured VS Code + Python extension
- Connected Git & GitHub for version control
- Mastered user input and f-string formatting

**Project: Greeting Program**
```python
# Greeting Program
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to my Python journey.")
```

**Concepts Learned**
- User input (`input()`)
- Variables and f-strings
- Basic program structure

---

### Session 02 — Conditions & Logic Flow
**Date:** March 5, 2026  
**Focus:** Decision-making and robust input validation

**Accomplishments**
- Implemented `if`/`elif`/`else` logic
- Added comprehensive input validation
- Built nested conditional structures

**Project: Grade Calculator**
```python
# Grade Calculator with Data Validation
marks = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Error: Please enter a number between 0 and 100.")
else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
```

**Concepts Learned**
- Conditional statements
- Logical operators (`and`, `or`)
- Input validation techniques

---

### Session 03 — Loops & Iteration
**Date:** March 6, 2026  
**Focus:** Repetition and interactive game logic

**Accomplishments**
- Mastered `for` loops and `range()`
- Used `break` for early exit
- Discovered `for-else` construct

**Project: Number Guessing Game**
```python
import random

number = random.randint(1, 100)
guess = 0

for i in range(5):
    guess = int(input(f"Attempt {i+1}/5 || Enter the guessed number: "))

    if guess == number:
        print("You Won!")
        break
    elif guess < number:
        print("Guess Higher")
    else:
        print("Guess Lower")
else:
    print(f"You are out of chances! The Number was {number}")
```

**Concepts Learned**
- `random` module
- Loop control (`break`)
- `for-else` behavior

---

### Session 04 — Lists & CLI Task Manager
**Date:** March 7, 2026  
**Focus:** Dynamic data storage and menu-driven interfaces

**Accomplishments**
- Deep dive into Python lists
- Implemented `append()`, `remove()`, `sort()`
- Built full CLI application with `enumerate()`

**Project: Task Manager CLI**
```python
tasks = []

while True:
    print("-------------Tasks Manager-------------") 
    print("1.Add 2.Remove 3.View 4.Sort 5.Exit")
    choice = input("Enter the choice: ").lower()
    
    if choice in ["1", "add"]:
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print("Task Added")
    elif choice in ["2", "remove"]:
        if tasks:
            print(f"Your tasks: {tasks}")
            remove_task = input("Enter the task to remove: ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print("Task removed!")
            else:
                print("Task not found")
        else:
            print("Nothing to remove")
    elif choice in ["3", "view"]:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
    elif choice in ["4", "sort"]:
        tasks.sort()
        print("Tasks sorted!")
    elif choice in ["5", "exit"]:
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
```

**Concepts Learned**
- List methods and operations
- `while True` menu loops
- `enumerate()` for indexed output

---

### Session 05 — Dictionaries & Inventory Tracker
**Date:** March 8, 2026  
**Focus:** Key-value data structures and real-world inventory management

**Accomplishments**
- Mastered dictionary operations
- Implemented search and update logic
- Added conditional alerts (out-of-stock)

**Project: Inventory Tracker CLI**
```python
inventory = {"phone": 5, "laptop": 2}

while True:
    print("--- SHOP INVENTORY ---")
    print("1. Add/Update  2. Check Stock  3. View All  4. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        item = input("Enter item name: ").lower()
        quantity = int(input(f"Enter quantity for {item}: "))
        inventory[item] = quantity
        print(f"Updated {item}. Total stock: {inventory[item]}")

    elif choice == '2':
        item = input("Search for item: ").lower()
        if item in inventory:
            count = inventory[item]
            if count == 0:
                print(f"ALERT: {item.capitalize()} is Out of Stock!")
            else:
                print(f"{item.capitalize()} stock: {count}")
        else:
            print("Item not found in inventory.")

    elif choice == '3':
        print("\nCurrent Inventory List:")
        for item, count in inventory.items():
            status = "OUT OF STOCK" if count == 0 else count
            print(f"- {item.capitalize()}: {status}")

    elif choice == '4':
        print("Closing tracker...")
        break
    else:
        print("Invalid choice.")
```

**Concepts Learned**
- Dictionaries (`dict`)
- `.items()` iteration
- Dynamic key-value updates
- Conditional inventory logic

---

## 🛠 Tools & Technologies

**Primary Stack**
- **Python 3.12** – Core language
- **VS Code** – Editor with Python extension
- **Git & GitHub** – Version control & portfolio hosting

**Additional Skills in Progress**
- SQL
- Excel Automation (openpyxl / pandas planned)

---

## 🎯 Long-Term Goals

- Build production-grade automation tools
- Develop freelance-ready data cleaning & reporting scripts
- Reach $800+ monthly income from Python freelancing
- Master Excel ↔ Python integration pipelines

---

## 💻 Languages & Stats

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Mahfeed&layout=compact&theme=tokyonight)

![Tech Stack](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tech Stack](https://img.shields.io/badge/sql-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)
![Tech Stack](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Tech Stack](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

![Contribution Snake](https://github.com/Mahfeed/Python-Portfolio/blob/main/github-user-contribution.svg)

---

⭐ **Follow my journey** as I transform from learner to professional Python automation engineer. Real projects, clean code, and consistent progress.

*Last updated: March 16, 2026*
```