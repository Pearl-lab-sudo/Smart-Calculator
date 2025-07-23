import math
import logging
from datetime import datetime

# --- Setup Logging ---
logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Safe Functions ---
safe_functions = {
    "abs": abs,
    "round": round,
    "square": lambda x: x * x,
    "cube": lambda x: x * x * x,
    "sqrt": math.sqrt,
    "power": pow,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e
}

def safe_eval(expression):
    try:
        result = eval(expression, {"__builtins__": None}, safe_functions)
        logging.info(f"Input: {expression} => Output: {result}")
        return result
    except Exception as e:
        logging.error(f"Error evaluating expression '{expression}': {e}")
        return f"Error: {str(e)}"

# --- Smart Calculator ---
def calculator():
    print("Welcome to the Smart Calculator!")
    print("Supports +, -, *, /, (), and functions: square(x), cube(x), sqrt(x), power(x)")
    print("Type 'exit' to quit the calculator.\n")

    while True:
        expression = input("Enter your expression: ")
        if expression.lower() == 'exit':
            print("Exiting the calculator. 👋🏿 Goodbye!")
            break

        result = safe_eval(expression)
        print("Result:", result)
calculator()