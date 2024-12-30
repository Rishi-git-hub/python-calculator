import os  # Import the os module for clearing the screen

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
clear_screen()  # Clear screen at the start
print("Welcome to the Basic Calculator!")

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number of the operation (1/2/3/4): ")

# Perform the operation
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation selected. Please try again!")

# Clear screen before exiting
input("\nPress Enter to clear the screen and exit...")
clear_screen()
