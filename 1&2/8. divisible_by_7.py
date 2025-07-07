'''a program that identifies and displays numbers within a specified range that are 
divisible by 7 but are not multiples of 5. It first performs this check 2000 to 3200
and then offers the user the option to perform the same check on a custom-defined range.'''

import os; 'importing to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear'); 'Function to clear the screen'

# to input two values from the user
def two_user_input():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            displayError()

# finds numbers within a specified range that are divisible by 7 but not a multiple of 5.
def numbersFinder(num1 = 2000, num2 = 3200):
    numbers = []
    for number in range(num1, num2 + 1):
        if number % 7 == 0 and number % 5 != 0:
            numbers.append(number)

    if len(numbers) != 0:
        print(f"Numbers divisible by 7 but not multiples of 5 between {num1} and {num2} are: ")
        for i in range(len(numbers)):
            print(numbers[i], end = " ")
        print() # to print an extra empty line

    else: # displays error if none of the numbers fulfill the criteria
        displayError()

def main():
    # first runs the program with default values
    numbersFinder()
    print()

    # then asks the user if they want customized values
    while True:
        ans = input("Do you want to find the numbers in customized range? (y/n) " )
        if ans in ['y', 'n']:
            if ans == 'y': # if yes, the program runs with new values
                clearScreen()
                num1, num2 = two_user_input()
                numbersFinder(num1, num2)
            else:
                print("Exited...")
                break

# Run the program
if __name__ == "__main__":
    main()