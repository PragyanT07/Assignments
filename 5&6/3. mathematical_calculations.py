'''a program that takes a list of numbers from the user, performs addition, subtraction,
multiplication, and division, and writes the results to a file with the current date and time.
users can repeat operations and view file contents upon exit.'''

import os; 'importing for file path operations'
from datetime import datetime; 'importing to get current date and time'

# to input the numbers
def user_imput():
    while True:
        user_input = input("enter a list of numbers separated by spaces: ")
        try:
            numbers = [float(x) for x in user_input.strip().split()]
            if len(numbers) < 2:
                print("please enter at least two numbers.")
                continue # ask again if less than two numbers
            return numbers # return valid list of numbers
        
        except ValueError:
            print("invalid input. please enter only numbers.") # error for non-numeric input

# to execute the mathematical operations

def calculate_operations(numbers):
    addition_result = sum(numbers) # sum of all numbers
    
    subtraction_result = numbers[0] # start subtraction with the first number
    for n in numbers[1:]:
        subtraction_result -= n # subtract subsequent numbers
    
    multiplication_result = 1 # start multiplication with 1
    for n in numbers:
        multiplication_result *= n # multiply all numbers
    
    division_result = numbers[0] # start division with the first number
    try:
        for n in numbers[1:]:
            # check for division by zero for each subsequent number
            if n == 0:
                raise ZeroDivisionError("division by zero encountered.")
            division_result /= n # divide by subsequent numbers
    except ZeroDivisionError:
        division_result = 'undefined (division by zero)' # set to string on error
    
    return addition_result, subtraction_result, multiplication_result, division_result

# writes the numbers and calculation results to the specified file appends to the file with a timestamp
def write_to_file(filename, numbers, results):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get current date and time

    with open(filename, 'a') as f: # open file in append mode
        f.write(f"date/time: {now}\n") # write timestamp
        f.write(f"numbers: {numbers}\n") # write input numbers
        f.write(f"addition: {results[0]}\n") # write addition result
        f.write(f"subtraction: {results[1]}\n") # write subtraction result
        f.write(f"multiplication: {results[2]}\n") # write multiplication result
        f.write(f"division: {results[3]}\n") # write division result
        f.write("-"*40 + "\n\n") # separator for readability

# reads and prints the entire content of the specified file handles file not found error.
def display_file(filename):
    if not os.path.exists(filename):
        print(f"no records found in '{filename}'.") # message if file doesn't exist
        return
    print(f"\n--- all calculations in '{filename}' ---\n")

    try:
        with open(filename, 'r') as f: # open file in read mode
            print(f.read()) # print file content
    except Exception as e:
        print(f"an error occurred while reading the file: {e}") # catch other read errors

# main block to execute the program
def main():
    filename = "calculations.txt" # default filename for storing results
    print("--- arithmetic operations to file ---")
    while True: # loop for continuous operations
        numbers = user_imput() # get numbers from user
        results = calculate_operations(numbers) # calculate results
        write_to_file(filename, numbers, results) # write results to file
        
        cont = input("do you want to perform another operation? (y/n): ").strip().lower() # ask to continue
        if cont != 'y':
            break # exit loop if user doesn't want to continue
    
    display_file(filename) # display all records from the file upon exit

# Running the code
if __name__ == "__main__":
    main()
