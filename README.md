# 🧠 Smart Calculator

A **terminal-based smart calculator** built with Python that allows users to perform arithmetic operations and advanced mathematical functions like square, cube, square root, and power. The calculator supports **safe function evaluation** and is interactive through user input.

---

## ✨ Features

- ✅ Basic arithmetic: `+`, `-`, `*`, `/`, `()`
- 🧮 Custom math functions: `square(x)`, `cube(x)`, `sqrt(x)`, `power(x, y)`
- 📐 Trigonometry: `sin(x)`, `cos(x)`, `tan(x)`
- 🔢 Math constants: `pi`, `e`
- ⚠️ Safe expression evaluation (no `eval()` injection risk)
- 📝 Logs all input expressions and errors to a log file
- Graceful exit with `'exit'` keyword

---

## 📁 Project Structure

smart_calculator/

│

├── smart_calculator.py # Main Python file

└── README.md # Documentation (this file)

---

## ▶️ How to Run

1. **Clone or download** the repository.
2. Open your terminal and navigate to the project directory.
3. Run the calculator with:

```bash
python smart_calculator.py
```
4. You’ll be prompted to enter an expression. Example:
square(5) + power(2, 3)
5. To exit the calculator, type:
```bash
exit
```
## 🧠 Example Usage
Enter your expression: square(4)
Result: 16

Enter your expression: sin(pi / 2)
Result: 1.0

Enter your expression: power(2, 5)
Result: 32

Enter your expression: exit
Calculator closed. Goodbye!

---
## 🔐 Safe Evaluation
Instead of the insecure eval(), we use:
eval(expression, {"__builtins__": None}, safe_functions)

---
## 📂 Logging
All user inputs and errors are logged in calculator.log.

Example log entries:
2025-07-21 06:45:23,001 - INFO - Input: square(5) => Output: 25
2025-07-21 06:45:24,013 - ERROR - Error evaluating expression 'abc(5)': name 'abc' is not defined

---

## 🔧 Improvements for Future
- GUI version using Tkinter or web version with Streamlit.
---
## 👨‍💻 Author
Lady Pearl Opoku

📫 Connect on LinkedIn : https://www.linkedin.com/in/ladypearlopoku/

---

## 🤝 Contributions
Feel free to fork, modify, and contribute to make the Smart Calculator even smarter!
