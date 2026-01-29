# Calculator Program for AICT Assignment 4
print("Simple Calculator")
print("Operations: +, -, *, /")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation: ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print(f"Result: {result}")
