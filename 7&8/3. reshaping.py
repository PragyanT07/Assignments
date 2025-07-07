'''a program that generates a random numpy array, sorts it,
and reshapes it into all possible 2d matrices based on its size. '''

import numpy as np; 'import numpy for array operations'

# # finds all pairs of factors for a given number n.
def find_factors(n):
    factors = [] # list to store factor pairs

    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0: # if i is a factor
            factors.append((i, n // i)) 
            if i != n // i: # generates a random array, sorts it, and reshapes it into all
                factors.append((n // i, i))
                
    return factors # return all factor pairs

# generates a random array, sorts it, and reshapes it into all
def perform_reshaping():
    
    try:
        array_size = 20 # define the size of the array
        # generate an array of 'array_size' random integers between 1 and 100
        original_array = np.random.randint(1, 101, size=array_size)
        
        # sort the array in ascending order
        sorted_array = np.sort(original_array)
        
        print("--- numpy array reshaping ---")
        print(f"original sorted array (1x{array_size}):\n{sorted_array}")
        print("---------------------------------")
        
        # find all feasible dimensions (factor pairs) for reshaping
        feasible_dimensions = find_factors(array_size)
        
        print("performing reshaping into all feasible matrix dimensions:")
        for rows, cols in sorted(feasible_dimensions): # sort dimensions for consistent output
            # skip reshaping into 1d arrays (e.g., 1x20 or 20x1) as it's the original shape
            if rows == 1 or cols == 1:
                continue
            
            # reshape the sorted array into the new dimensions
            reshaped_matrix = sorted_array.reshape(rows, cols)
            
            print(f"\nreshaped into a {rows}x{cols} matrix:")
            print(reshaped_matrix)
            
        print("\n---------------------------------")

    except Exception as e:
        # general error handling for unexpected issues
        print(f"\nan unexpected error occurred: {e}")

# main part of the program
if __name__ == "__main__":
    perform_reshaping() # execute the reshaping process
