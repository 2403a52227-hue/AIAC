# Simple Calculator Script with Add, Subtract, Multiply, and Divide Functions

# Function to add two numbers
def add(a, b):
    return a + b  # Return the sum

# Function to subtract two numbers
def subtract(a, b):
    return a - b  # Return the difference

# Function to multiply two numbers
def multiply(a, b):
    return a * b  # Return the product

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"  # Handle division by zero
    return a / b  # Return the quotient

# Main program starts here
print("Simple Calculator")
print("Select operation: add, subtract, multiply, divide")

# Get operation from user
operation = input("Enter operation: ").strip().lower()

# Get numbers from user and convert to float
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation selected"

# Print the result
print("Result:", result)