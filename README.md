![Python](https://img.shields.io/badge/Python-Learning-blue)
![Status](https://img.shields.io/badge/Progress-Active-green)
![Goal](https://img.shields.io/badge/Goal-Python%20Automation-orange)
# 🐍 Python Automation Journey

> **Goal:** Master Python for **Automation, Data Cleaning, and Freelancing Projects** — one midnight coding session at a time.

---
## 📅 Learning Log

Mar 4 — Environment setup & Greeting Program  
Mar 5 — Grade Calculator  
Mar 6 — Number Guessing Game

# 🚀 Project Roadmap

Tracking my daily progress as I build practical Python automation skills.

| Session | Topic                      | Status     | Project              |
| ------- | -------------------------- | ---------- | -------------------- |
| **01**  | Environment Setup & Basics | ✅ Complete | Greeting Program     |
| **02**  | Conditions & Logic Flow    | ✅ Complete   | Grade Calculator     |
| **03**  | Loops & Iteration          | ✅ Complete | Number Guessing Game |
| **04** | Lists & CLI Programs | ✅ Complete | Task Manager |
| **05**  | File Handling              | ⏳ Upcoming | CSV Data Cleaner     |

---

# 📊 Learning Progress

```
Python Fundamentals     ██████████ 95%
Automation Skills       ████░░░░░░ 35%
Data Cleaning           ██░░░░░░░░ 20%
Freelancing Ready       █░░░░░░░░░ 5%
```

---

# 🌙 Session 1 — The Basics

📅 **Date:** March 4, 2026
🎯 **Focus:** Python setup and core syntax

## ✅ Accomplishments

* Installed **VS Code**
* Configured **Python Extension**
* Connected **Git & GitHub**
* Learned **user input and f-strings**

## 🚀 Project: Greeting Program

My first dynamic Python script.

```python
# Greeting Program
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to my Python journey.")
```

💡 **Concepts Learned**

* User input
* Variables
* f-string formatting

---

# 🌙 Session 2 — Conditions & Logic Flow

📅 **Date:** March 5, 2026
🎯 **Focus:** Decision making and input validation

## ✅ Accomplishments

* Learned `if`, `elif`, `else`
* Implemented **input validation**
* Practiced **nested logic**
* Built a practical mini-project

## 🚀 Project: Grade Calculator

A script that evaluates student performance while ensuring valid input.

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

💡 **Concepts Learned**

* Conditional statements
* Logical operators
* Input validation
* Nested decision structures

---

# 🧰 Tools I Use

* 💻 **VS Code**
* 🐍 **Python 3**
* 🌐 **Git & GitHub**

---

# 🎯 Long Term Goals

✔ Build **Python automation tools**
✔ Create **data cleaning scripts for freelancers**
✔ Earn **$800+ from Python freelancing projects**
✔ Master **Excel + Python automation**

---
---

# 🌙 Session 3 — Loops & Iteration

📅 **Date:** March 6, 2026
🎯 **Focus:** Using loops to create interactive programs and simple games.

## ✅ Accomplishments

* Learned `for` loops
* Implemented multiple attempts using loop iteration
* Used `break` to exit loops early
* Discovered Python's `for-else` behavior
* Built an interactive CLI game

## 🚀 Project: Number Guessing Game

A simple terminal game where the user must guess a randomly generated number within **5 attempts**.

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

💡 **Concepts Learned**

* `random` module
* `for` loops
* conditional logic
* `break` statement
* `for-else` loop structure

---

## 🌙 Session 4 — Lists & CLI Task Manager 📝

📅 **Date:** March 7, 2026
🎯 **Focus:** Using lists and loops to build a simple command-line task manager.

### ✅ Accomplishments

* Learned **Python lists** for storing data
* Used `append()` to add items dynamically
* Implemented **task removal**
* Used `enumerate()` to display numbered tasks
* Added **sorting functionality**
* Built a full **menu-driven CLI application**

### 🚀 Project: Task Manager CLI

A simple terminal-based task manager that allows the user to:

* Add tasks
* Remove tasks
* View all tasks
* Sort tasks alphabetically
* Exit the program

```python
tasks = []

while True:
    print("-------------Tasks Manager-------------") 
    print("1.Add 2.Remove 3.View 4.Sort 5.Exit")
    choice = input("Enter the choice: ").lower()
    
    if choice == "1" or choice == "add":
        new_task = input("Enter the new task:")
        tasks.append(new_task)
        print("Task Added")

    elif choice == "2" or choice == "remove":
        if len(tasks) > 0:
            print(f"your tasks : {tasks}")
            remove_task = input("Enter the task to remove : ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print("task removed!")
            else:
                print("not found")
        else:
            print("nothing to remove")

    elif choice == "3" or choice == "view":
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}.{task}")

    elif choice == "4" or choice == "sort":
        tasks.sort()
        print("Tasks sorted!")

    elif choice == "5" or choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
```

💡 **Concepts Learned**

* Python lists
* List methods (`append`, `remove`, `sort`)
* `while` loops
* Menu-driven programs
* `enumerate()` for indexed output

---


# 📌 Current Focus

```
Learning → Practicing → Building → Freelancing
```

---

## 💻 Languages I Use

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Mahfeed&layout=compact&theme=tokyonight)
## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-Automation-blue)
![SQL](https://img.shields.io/badge/SQL-Database-green)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange)
![VS Code](https://img.shields.io/badge/Editor-VSCode-purple)

![Snake animation](https://github.com/Mahfeed/Python-Portfolio/blob/main/github-user-contribution.svg)

⭐ *Follow my journey as I build real Python tools and automation scripts.*
