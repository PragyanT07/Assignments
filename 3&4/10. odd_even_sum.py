'''a program that continuously prompts the user to input numbers until they choose to stop.
It segregates the entered numbers into two separate lists: one for even numbers
and one for odd numbers. Upon exiting, the program displays both the even and
odd number lists in a formatted manner.
'''

import os; 'importing to clear the screen'

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear'); 'Function to clear the screen'

def even_or_odd():
    even = [] # list to add even numbers
    odd = [] # list to add odd numbers

    while True:
            try: 
                num = int(input("Enter a number: "))

                # checking and adding number into the respective list
                if num % 2 == 0:
                    even.append(num)
                else:
                    odd.append(num)

                while True:
                    ans = input("Do you want to continue? (y/n) ") # asking user to continue or not

                    if ans in ["y", "n"]:
                            break
                    else:
                        print("Please enter 'y' for yes and 'n' for no.")

                if ans == "n": # if no then then exits the program
                    clearScreen()
                    print(f"The list of even numbers:\n{even}")
                    print(f"The list of odd numbers:\n{odd}")
                    break
                
                clearScreen()

            except ValueError:
                print("Please enter a valid integer")

even_or_odd()