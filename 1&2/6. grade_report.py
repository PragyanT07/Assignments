'''a program that prompts the user to enter marks for five subjects,calculates the
total marks, average marks, and percentage along with the student's division'''

import os; 'Import to clear the screen'

# to print the error message
def displayError():
    print("Error: Please enter valid value")

# to clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear'); 'Function to clear the screen'

# to input marks of the 5 subjects from the user
def user_input():
    marks = []
    for i in range(1, 6): 
        while True: # Loop until valid input for the current subject is received
            try:
                mark_str = input(f"Enter the marks of subject {i} (out of 100): ")
                mark = float(mark_str)
                
                # Validate if marks are within the acceptable range (0 to 100)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break # Exit inner loop if mark is valid
                else:
                    displayError()
            except ValueError:
                displayError()
    
    return marks[0], marks[1], marks[2], marks[3], marks[4]

# gets marks for five subjects, calculates total, average, percentage, and determines the student's division
def main():
    num1, num2, num3, num4, num5 = user_input()
    clearScreen()
    
    total = (num1 + num2 + num3 + num4+ num5)
    average = total / 5
    percentage = (total/500) * 100

    if percentage > 80:
        division = "Distinction"
    elif percentage > 60:
        division = "First"
    elif percentage > 50:
        division = "Second"
    elif percentage > 45:
        division = "Third"
    else:
        division = "Fail"
    
    print("--- Student Grade Report ---")
    print(f"Marks entered:")
    print(f"Subject 1: {num1:.2f}")
    print(f"Subject 2: {num2:.2f}")
    print(f"Subject 3: {num3:.2f}")
    print(f"Subject 4: {num4:.2f}")
    print(f"Subject 5: {num5:.2f}")
    print(f"The total marks is: {total:.2f}")
    print(f"The average marks is: {average:.2f}")
    print(f"The percentage is: {percentage:.2f}%")
    print(f"Division: {division}")

# Run the program
if __name__ == "__main__":
    main()
