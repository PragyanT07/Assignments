'''a program that defines separate functions for various arithmetic operations, takes two numbers
 as input from the user, and then uses these functions to calculate and display the sum, difference, 
 product, division, modulo, and floor division results.
'''

# to add two numbers
def addition(num1, num2):
    sum = num1 + num2
    return sum

# to subtract two numbers
def subtraction(num1, num2):
    difference = num1 - num2
    return difference

# to multiply two numbers
def multiplication(num1, num2):
    product = num1 * num2
    return product

# to divide two numbers and even check for division by zero
def division(num1, num2):
    try:
        division = num1 / num2
        return division
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# to modulo divide two numbers and even check for division by zero
def modulo_division(num1, num2):
    try:
        modulo_division = num1 % num2
        return modulo_division
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# to floor divide two numbers and even check for division by zero
def floor_division(num1, num2):
    try:
        division = num1 // num2
        return division
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
# main block of the program
if __name__ == "__main__":
    # Loop to get valid user input for two numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break # If both conversions are successful, break the loop
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    
    # Call each function and display its returned result directly
    print(f"\nAddition: {addition(num1, num2):.2f}")

    print(f"Subtraction: {subtraction(num1, num2):.2f}")

    print(f"Multiplication: {multiplication(num1, num2):.2f}")

    # Check if division returned an error string or a number
    div_val = division(num1, num2)

    if isinstance(div_val, str):
        print(f"Division: {div_val}")
    else:
        print(f"Division: {div_val:.2f}")

    mod_val = modulo_division(num1, num2)
    if isinstance(mod_val, str):
        print(f"Modulo Division: {mod_val}")
    else:
        print(f"Modulo Division: {mod_val:.2f}")

    floor_div_val = floor_division(num1, num2)
    if isinstance(floor_div_val, str):
        print(f"Floor Division: {floor_div_val}")
    else:
        print(f"Floor Division: {floor_div_val:.2f}")


