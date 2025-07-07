'''a program that provides a menu-driven interface for performing various
exponential and logarithmic functions on a user-input number.'''

import os; 'import to clear the screen'
import math; 'import for using square root and logarithm'

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear'); 'Function to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to input one float value from the user
def user_input():
    while True:
        try:
            num1 = float(input("Enter a number: "))
            return num1
        except ValueError:
            displayError()

# to find the square of the number
def square():
    num1 = user_input()
    square = num1 ** 2
    print(f"The square of {num1} is: {square:.2f}")

# to find the square root of the number and validate the input if its negative or not
def square_root():
    num1 = user_input()
    if num1 < 0:
        print("Square root of a negative number is not possible.")
    else:
        square_root = math.sqrt(num1)
        print(f"The square root of {num1} is: {square_root:.2f}")

# to find the exponent of the number (num raised to another exponent)
def exponent():
    while True: 
        try:
            base = float(input("Enter the base number: "))
            power_val = float(input("Enter the exponent: "))
            break # Exit loop if both inputs are valid
        except ValueError:
            displayError()

    exponent = base ** power_val
    print(f"The exponent value of {base} to the power of {power_val} is: {exponent:.2f}")

# to find the log base 10 of the number and also validate if the input is negative or not
def logarithm():
    num1 = user_input()
    if num1 <= 0:
        print("Logarithm of a negative number is not possible.")
    else:
        logarithm = math.log10(num1) # math.log10 is specifically for base 10
        print(f"The log base 10 of {num1} is: {logarithm:.2f}")

# to find the third, fourth and fifth power of the number
def power():
    num1 = user_input()
    power_3 = num1 ** 3
    power_4 = num1 ** 4
    power_5 = num1 ** 5
    print(f"The power 3 of {num1} is: {power_3:.2f}")
    print(f"The power 4 of {num1} is: {power_4:.2f}")
    print(f"The power 5 of {num1} is: {power_5:.2f}")

# a menu-driven main function to let the user choose the intended operation
def main():
    while True:
        clearScreen()
        print("Choose the operation to be performed:")
        print("1. Square of a number")
        print("2. Square root of a number")
        print("3. Exponent value with the number")
        print("4. Log base 10 of the number")
        print("5. The third, fourth and fifth power of the number")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        clearScreen()

        if choice == '1':
            square()
        elif choice == '2':
            square_root()
        elif choice == '3':
            exponent()
        elif choice == '4':
            logarithm()
        elif choice == '5':
            power()
        elif choice == '6':
            print("Exiting the program...")
            break # exiting the loop
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to go back to the menu.")

# Run the program
if __name__ == "__main__":
    main()
