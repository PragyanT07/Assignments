'''a menu-driven program that takes two numbers as input from the user and performs six basic arithmetic operations: 
addition, subtraction, multiplication, division, modulo division, and floor division. The results are then
displayed in a clear, formatted manner. '''

import os; 'importing os to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# to prompt user for two input values and checking whether the value is valid or not
def user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            displayError()

# to add two numbers
def addition():
    num1, num2 = user_input()
    addition = num1 + num2
    print(f"The sum of {num1} and {num2} is: {addition:.2f}")

# to subtract two numbers
def subtraction():
    num1, num2 = user_input()
    subtraction = num1 - num2
    print(f"The difference between {num1} and {num2} is: {subtraction:.2f}")

# to multiply two numbers
def multiplication():
    num1, num2 = user_input()
    multiplication = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {multiplication:.2f}")

# to divide two numbers and even check for division by zero
def division():
    num1, num2 = user_input()
    try:
        division = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {division:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# to modulo divide two numbers and even check for division by zero
def modulo_division():
    num1, num2 = user_input()
    try:
        modulo_division = num1 % num2
        print(f"The result of modulo division between {num1} and {num2} is: {modulo_division:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# to floor divide two numbers and even check for division by zero
def floor_division():
    num1, num2 = user_input()
    try:
        floor_division = num1 // num2
        print(f"The result of floor division between {num1} and {num2} is: {floor_division:.2f}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# presents a menu of operations to the user and performs the chosen operation and continues until the user chooses to exit
def main():
    # a continuous loop until the user wants to exit
    while True:
        clearScreen()
        print("Choose the operation to be performed:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo Division")
        print("6. Floor Division")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        clearScreen()

        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            modulo_division()
        elif choice == '6':
            floor_division()
        elif choice == '7':
            print("Exiting the program...")
            break # exiting the main loop
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to go back to the menu.")

# Run the program
if __name__ == "__main__":
    main()