'''a program that takes an array of numbers from the user, sorts it,
and performs slicing operations to extract elements from specific index ranges.'''

import numpy as np; 'import numpy for array operations'
import os; 'import os for screen clearing'

def clearScreen():
    # clears the console screen.
    os.system('cls' if os.name == 'nt' else 'clear')

# to get input from the user
def get_user_array():
    numbers = [] # list to store user numbers
    print("please enter at least 10 numbers. type 'done' when you are finished.")
    
    while True: # loop to get continuous input
        user_input = input(f"enter number {len(numbers) + 1}: ")
        
        if user_input.lower() == 'done': # check for exit command
            if len(numbers) < 10:
                print(f"error: you must enter at least 10 numbers. you have entered {len(numbers)}.")
                continue # continue loop if not enough numbers
            else:
                clearScreen() # clear screen before breaking
                break # exit input loop
        
        try:
            numbers.append(float(user_input)) # convert input to float and add to list
        except ValueError:
            print("invalid input. please enter a valid number or 'done'.") # error for non-numeric input
            
    return np.array(numbers) # convert list to numpy array

# sorts the given numpy array and performs slicing operations
def perform_slicing(arr):
    
    try:
        sorted_arr = np.sort(arr) # sort the array
        print("\n--- array slicing operations ---")
        print(f"original array: {arr}")
        print(f"sorted array:   {sorted_arr}")
        print("--------------------------------")

        # perform slicing operations as specified
        slice_2_5 = sorted_arr[2:6] # elements from index 2 up to (but not including) 6
        slice_5_8 = sorted_arr[5:9] # elements from index 5 up to (but not including) 9
        slice_2_9 = sorted_arr[2:10] # elements from index 2 up to (but not including) 10

        print(f"elements from index 2 to 5: {slice_2_5}")
        print(f"elements from index 5 to 8: {slice_5_8}")
        print(f"elements from index 2 to 9: {slice_2_9}")
        print("--------------------------------")

    except IndexError:
        # handle error if array is too small for requested slices
        print("\nan error occurred. the array is not large enough for the requested slicing operations.")
    except Exception as e:
        # general error handling
        print(f"\nan unexpected error occurred: {e}")

# main execution block
if __name__ == "__main__":
    user_array = get_user_array() # get array from user
    perform_slicing(user_array) # perform slicing operations