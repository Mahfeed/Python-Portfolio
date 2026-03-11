# 🐍 Python Journey | Portfolio & Logs
> **Goal:** Mastering Python for automation and data cleaning, one midnight at a time.

---

## 📈 Progress Overview
| Session | Focus | Status | Featured Project |
| :--- | :--- | :--- | :--- |
| **01** | Environment Setup & Basics | ✅ Complete | [Greeting Program](#-session-1-the-basics) |
| **02** | Conditions & Logic Flow | 🏗️ In Progress | [Grade Calculator](#-session-2-conditions--logic-flow) |

---
## 🌙 Session 1: The Basics
**Date:** March 4, 2026
**Focus:** Toolchain installation and core syntax.

### ✅ Accomplishments
- [x] Installed **VS Code** and configured the **Python Extension**.
- [x] Established the **Git/GitHub** connection for version control.
- [x] Mastered basic input handling and modern `f-string` formatting.

### 🚀 Featured Project: Greeting Program
```python
# My first dynamic script
name = input("What is your name? ")
print(f"Hello, {name}!")

## 🌙 Session 2: Conditions & Logic Flow ![Status](https://img.shields.io/badge/Status-Active-brightgreen)
**Date:** March 5, 2026
**Focus:** Building "intelligent" scripts that handle real-world data edge cases.

### ✅ Accomplishments
- [x] Mastered `if`, `elif`, and `else` structures for decision making.
- [x] Implemented **Input Validation** to prevent processing of "dirty data" (marks < 0 or > 100).
- [x] Learned **Nested Logic** to ensure clean output and prevent execution errors.

### 🚀 Featured Project: Grade Calculator
A robust script that categorizes student performance while sanitizing user input.

```python
# Grade Calculator with Data Validation
marks = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Error: Please enter a number between 0 and 100.")
else:
    # Logic only executes if data is valid
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