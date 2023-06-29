#basic calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        return None

print("Welcome to the Calculator Program!")

while True:
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the Calculator Program. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("The result of addition is:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The result of subtraction is:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The result of multiplication is:", result)
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print("The result of division is:", result)
    else:
        print("Invalid choice! Please try again.")
