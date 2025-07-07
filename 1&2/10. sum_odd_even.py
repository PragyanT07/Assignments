'''a program that continuously takes integer inputs from the user and maintains two separate running sums:
one for odd numbers entered and one for even numbers entered. The program is menu-driven,allowing the user 
to choose to continue entering numbers or exit to view the final sums of both odd and even numbers.'''

import os; 'Importing os to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Allows continuous input of numbers, categorizes them as odd or even,
# and maintains separate running sums for each category.
def main():
    total_even_sum = 0 
    total_odd_sum = 0  

    while True: # Main loop to continue the program until user exits
        clearScreen() 
        print("Select an option:")
        print("1. Enter a number")
        print("2. Exit and view final sums")

        choice = input("Enter your choice (1-2): ")
        clearScreen() # Clear screen after choice

        if choice == '1':
            try:
                num = int(input("Enter an integer: "))

                # Check if the number is even or odd and add to respective sum
                if num % 2 == 0:
                    total_even_sum += num
                    print(f"'{num}' is an EVEN number. Added to even sum.")

                else:
                    total_odd_sum += num
                    print(f"'{num}' is an ODD number. Added to odd sum.")
                
                print(f"Current Sum of Even Numbers: {total_even_sum}")
                print(f"Current Sum of Odd Numbers: {total_odd_sum}")

            except ValueError:
                displayError()
            
            input("\nPress Enter to continue...") 

        elif choice == '2':
            print("--- Final Results ---")
            print(f"Total Sum of Even Numbers: {total_even_sum}")
            print(f"Total Sum of Odd Numbers: {total_odd_sum}")
            print("Thank you for using the program!")
            break # Exit the main loop

        else:
            displayError()
            input("\nPress Enter to go back to the menu.")

# Run the program
if __name__ == "__main__":
    main()
