'''a program that takes two matrices from the user, performs addition, subtraction, and multiplication 
using numpy; it includes validation for matrix dimensions for each operation.'''

import numpy as np; 'import numpy for matrix operations'
import os; 'import os for screen clearing'

def clearScreen():
    # clears the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')

# prompts the user to enter elements for a matrix of specified dimensions.
def get_matrix_from_user(rows, cols, matrix_name):
    print(f"\nenter the elements for matrix {matrix_name} ({rows}x{cols}):")
    matrix_elements = [] # list to temporarily store elements

    try:
        for i in range(rows):
            row = [] 
            for j in range(cols): 
                element = float(input(f"enter element at position ({i+1}, {j+1}): ")) # get element input
                row.append(element) # add element to row
            matrix_elements.append(row) # add row to matrix list
        return np.array(matrix_elements) # convert list of lists to numpy array
    
    except ValueError:
        print("\nerror: invalid input. please enter only numbers.") # error for non-numeric input
        return None # return none if input is invalid

# main function to run the matrix operations program
def main():
    try:
        # get dimensions for matrix a
        rows_a = int(input("enter the number of rows for matrix a: "))
        cols_a = int(input("enter the number of columns for matrix a: "))
        matrix_a = get_matrix_from_user(rows_a, cols_a, "a") # get matrix a from user

        clearScreen() # clear screen for matrix b input
        # get dimensions for matrix b
        rows_b = int(input("\nenter the number of rows for matrix b: "))
        cols_b = int(input("enter the number of columns for matrix b: "))
        matrix_b = get_matrix_from_user(rows_b, cols_b, "b") # get matrix b from user

        # if either matrix input was invalid, exit
        if matrix_a is None or matrix_b is None:
            return

        while True: # loop for matrix operations menu
            clearScreen() # clear screen for menu
            print("\n--- matrix operations menu ---")
            print("1. addition (+)")
            print("2. subtraction (-)")
            print("3. multiplication (*)")
            print("4. exit")
            
            choice = input("enter your choice (1-4): ") # get user's choice
            clearScreen() # clear screen after choice
            
            if choice == '1':
                # check if dimensions are same for addition
                if matrix_a.shape == matrix_b.shape:
                    result = matrix_a + matrix_b # perform addition
                    print("\nresult of addition (a + b):")
                    print(result)
                else:
                    print("\nerror: matrices must have the same dimensions for addition.") # error for dimension mismatch
            
            elif choice == '2':
                # check if dimensions are same for subtraction
                if matrix_a.shape == matrix_b.shape:
                    result = matrix_a - matrix_b # perform subtraction
                    print("\nresult of subtraction (a - b):")
                    print(result)
                else:
                    print("\nerror: matrices must have the same dimensions for subtraction.") # error for dimension mismatch

            elif choice == '3':
                # check if dimensions are compatible for multiplication (cols of a == rows of b)
                if matrix_a.shape[1] == matrix_b.shape[0]:
                    result = np.dot(matrix_a, matrix_b) # perform matrix multiplication
                    print("\nresult of multiplication (a * b):")
                    print(result)
                else:
                    print(f"\nerror: the number of columns in matrix a ({matrix_a.shape[1]}) must equal the number of rows in matrix b ({matrix_b.shape[0]}) for multiplication.") # error for dimension mismatch

            elif choice == '4':
                print("\nexiting program. goodbye.")
                break # exit menu loop
            
            else:
                print("\ninvalid choice. please enter a number between 1 and 4.") # error for invalid menu choice

            input("press enter to return to the menu") # pause for user to read output

    except ValueError:
        # handle error for non-integer input for dimensions
        print("\nerror: invalid input for dimensions. please enter only integers.")
    except Exception as e:
        # general error handling for unexpected issues
        print(f"\nan unexpected error occurred: {e}")

# main execution block
if __name__ == "__main__":
    main()
