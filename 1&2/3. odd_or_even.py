'''a program that prompts the user to input an integer and determines whether the number is even or odd'''

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to prompt the user to enter an integer and validates the input
def user_input():
    while True:
        try:
            num1 = int(input("Enter a number: "))
            return num1
        except ValueError:
            displayError()

# to run the even/odd number checker
def main():
    num1 = user_input()
    if num1 % 2 == 0:
        print(f"{num1} is an even number.")
    else:
        print(f"{num1} is an odd number.")

# run the program
if __name__ == "__main__":
    main()
