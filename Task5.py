# Simple Calculator Program

def add(a=0, b=0):
    return a + b

def subtract(a=0, b=0):
    return a - b

def multiply(a=0, b=0):
    return a * b

def divide(a=0, b=1):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        result = "Invalid choice!"
    print("Result:", result)

print("Testing functions:")
print("Add:", add(5, 3))
print("Subtract:", subtract(5, 3))
print("Multiply:", multiply(5, 3))
print("Divide:", divide(5, 3))
print("Divide by zero test:", divide(5, 0))

print("\nNow running calculator:\n")
calculator()
