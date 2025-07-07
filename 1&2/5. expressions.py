'''a program that provides a menu-driven interface to calculate the values of
three specific algebraic expressions based on user-provided variable inputs. '''

import os; 'import to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear'); 'Function to clear the screen'

# to input three float values from the user
def three_user_inputs(choice):
    while True:
        try:
            num1 = float(input("Enter the value of a: "))
            num2 = float(input("Enter the value of b: "))
            if choice == '1':
                return num1, num2
            else: # ask for the value of c only if needed
                num3 = float(input("Enter the value of c: "))
                return num1, num2, num3
        except ValueError:
            displayError()

# presents a menu of expressions to the user and calculates the value
# of the chosen expression based on user-provided variable inputs.
def main():
    while True:
        clearScreen()
        print("Choose an expression to find the value of:")
        print("1. a^2 + 2ab + b^2")
        print("2. a^5 + 2abc + b^3 + c^4")
        print("3. a^7 + 5a^3b^2c^6 + b^7")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        clearScreen()

        if choice == '1':
            a, b = three_user_inputs(choice)
            expression = (a ** 2) + (2 * a * b) + (b ** 2)
            print(f"The value of a^2 + 2ab + b^2 is:\n{expression:.2f}")

        elif choice == '2':
            a, b, c = three_user_inputs(choice)
            expression = (a ** 5) + (2 * a * b * c) + (b ** 3) + (c ** 4)
            print(f"The value of a^5 + 2abc + b^3 + c^4 is:\n{expression:.2f}")

        elif choice == '3':
            a, b, c = three_user_inputs(choice)
            expression = (a ** 7) + (5 * (a ** 3) * (b ** 2) * (c ** 6)) + (b ** 7)
            print(f"The value of a^7 + 5a^3b^2c^6 + b^7 is:\n{expression:.2f}")

        elif choice == '4':
            print("Exiting the program...")
            break # exiting the loop

        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to go back to the menu.")

# Run the program
if __name__ == "__main__":
    main()
