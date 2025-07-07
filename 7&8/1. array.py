'''a program that generates a numpy array and performs basic operations on it; 
operations include calculating the sum, average, maximum, and minimum values of the array elements.'''

import numpy as np; 'import numpy for array operations'

# performs sum, average, max, and min operations on a given numpy array
def perform_array_operations(arr):
    
    try:
        total_sum = np.sum(arr) # calculate sum of all elements
        average_value = np.mean(arr) # calculate average of elements
        max_value = np.max(arr) # find maximum value
        min_value = np.min(arr) # find minimum value

        print("--- numpy array operations ---")
        print(f"original array: {arr}")
        print("------------------------------")
        print(f"sum of elements:      {total_sum}")
        print(f"average of elements: {average_value:.2f}") # format average to 2 decimal places
        print(f"maximum value:        {max_value}")
        print(f"minimum value:        {min_value}")
        print("------------------------------")

    except Exception as e:
        print(f"an error occurred: {e}") # general error handling

# main execution block
if __name__ == "__main__":
    # test with a sample array
    array1 = np.array([1, 2, 3, 4, 5])
    perform_array_operations(array1)