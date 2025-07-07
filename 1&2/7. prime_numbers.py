'''a program that prompts the user to enter a number then finds and displays all prime 
numbers within  2 and that specified number and calculates their total sum.'''

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to input two values from the user
def user_input():
    while True:
        try:
            start= int(input("Enter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))

            if start > end:
                print("Error: The starting number cannot be greater than the ending number. Please try again.")
            else:
                return start, end # Return numbers if valid range
        except ValueError:
            displayError()

# to find and sum prime numbers within a user-defined range
def main():
    num1, num2 = user_input()
    prime_numbers = []
    total = 0

    for i in range(num1, num2 + 1):
        is_prime =  True
        if i <= 1: # checks if the number is one
            is_prime = False
        if i == 2: # checks if the number is two
            is_prime = True
        elif i % 2 == 0: # checks if divisible by two
            is_prime = False
        else:
            # loop through potential odd divisors, from 3 up to the square root of the number
            for j in range(3, int(i**0.5) + 1, 2): 
                if i % j == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_numbers.append(i)

    print(f"The prime numbers between {num1} and {num2} are:")

    for num in prime_numbers:
        print(num, end = " ") # prints each prime number 
        total += num # adds the prime numbers

    print(f"\nThe sum of the prime numbres between {num1} and {num2} is: {total}")

# Run the program
if __name__ == "__main__":
    main()