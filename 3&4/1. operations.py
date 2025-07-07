'''a program that defines a function to perform basic operations
(sum, difference, product, remainder) on two user-input numbers.'''

# accepts two numbers and displays their sum, difference, product, and remainder.
def operations(num1, num2):
    sum = num1 + num2

    difference = num1 - num2

    product = num1 * num2

    if num2 != 0:
        remainder = num1 % num2
    else: # Indicate error when divided by zero
        remainder = "Undefined (division by zero)" 

    print(f"The sum of {num1} and {num2} is: {sum}")
    print(f"The difference of {num1} and {num2} is: {difference}")
    print(f"The product of {num1} and {num2} is: {product}")
    print(f"The remainder while dividing {num1} by {num2} is: {remainder}")

# Running the program
if __name__ == "__main__":
    # Loop to get valid user input for two numbers
    while True:
        try:
            num1_str = input("Enter the first number: ")
            number1 = float(num1_str) # Convert input to float to handle decimals

            num2_str = input("Enter the second number: ")
            number2 = float(num2_str) # Convert input to float

            break 
        except ValueError:
            print("Error: Please enter valid numeric values.")
    
    operations(number1, number2)