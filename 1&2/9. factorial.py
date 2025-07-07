'''a program to find the factorial of the user prompted number 
but first making sure its a number with .isdigit() operator'''

# main function to calculate the factorial of a user-input number.
def main():
    while True: # Loop indefinitely until a valid non-negative integer is entered
        num = input("Enter a non-negative integer to calculate its factorial: ")

        if num.isdigit(): # checks if its a number or not
            num1 = int(num)

            if num1 == 0: # Factorial of 0 is 1
                print(f"The factorial of {num1} is 1")
                break # Exit loop 

            else: # Calculate factorial for positive integers
                factorial = 1
                for i in range(1, num1 + 1):
                    factorial *= i
                print(f"The factorial of {num1} is {factorial}")
                break # Exit loop 

        else: # prints an eroor message for non numeric inputs
            if num.isalpha():
                print("Not a number")
            else:
                print("Factorial is not defined for these numbers")

# Run the program
if __name__ == "__main__":
    main()