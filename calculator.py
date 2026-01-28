# Simple Calculator Program in Python
# Created for AICT Assignment 4
# Date: 28-01-2026

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function with error handling"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    """Main calculator program"""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("Operations: +, -, *, /")
    print("-" * 40)
    
    try:
        # User input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation!"
        
        # Display result
        print("-" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("=" * 40)

# Run the calculator
if __name__ == "__main__":
    main()
