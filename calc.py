# calc.py - Simple Calculator Module

def add(a, b):
 """Return the sum of a and b."""
 return a + b

def subtract(a, b):
 """Return the difference of a and b."""
 return a - b

def multiply(a, b):
 """Return the product of a and b."""
 return a * b

def divide(a, b):
 """Return the quotient of a and b. Raises ValueError if b is zero."""
 if b == 0:
 raise ValueError("Cannot divide by zero")
 return a / b

if __name__ == "__main__":
 # Simple CLI for testing
 import sys
 if len(sys.argv) != 4:
 print("Usage: python calc.py <operation> <num1> <num2>")
 print("Operations: add, subtract, multiply, divide")
 sys.exit(1)
 
 op, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
 
 operations = {
 "add": add,
 "subtract": subtract,
 "multiply": multiply,
 "divide": divide
 }
 
 if op not in operations:
 print(f"Unknown operation: {op}")
 sys.exit(1)
 
 result = operations[op](a, b)
 print(result)
