# Python-Portfolio
### 🚀 Featured Project: Greeting Program
This was my first script from Session 1!

```python
# Copy and paste your greeting.py code here
name = input("What is your name? ")
print(f"Hello, {name}!")

## 🌙 Session 2 Log: March 5, 2026
**Focus:** Conditions and Logic Flow.

### ✅ Accomplishments
- [x] Mastered `if`, `elif`, and `else` structures.
- [x] Built a **Grade Calculator** with data validation (catching scores > 100 or < 0).
- [x] Learned to nest logic to prevent "double execution" errors.

### 🚀 Featured Project: Grade Calculator
```python
# Validates input before assigning a grade
marks = int(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Error: Please enter a number between 0 and 100.")
else:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    else:
        print("Grade: F") # Simplified for README