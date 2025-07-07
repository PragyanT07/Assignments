'''a program that defines a function that accepts a number as a parameter
and calculates its factorial.'''

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    
    elif num == 0:
        return 1
    
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    # Loop indefinitely until a valid non-negative integer is entered
    while True: 
        try:
            num = int(input("Enter a non-negative integer to calculate its factorial: "))
            
            # Call the function to get the factorial result
            result = factorial(num)
            
            # Display the result based on what the function returned
            if isinstance(result, str): 
                print(f"Error: {result}")
            else:
                print(f"The factorial of {num} is: {result}")
            
            break 
            
        except ValueError:
            print("Error: Please enter a valid integer.")
