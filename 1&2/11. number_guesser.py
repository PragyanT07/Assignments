'''
Made by Pragyan Timalsina. Developed as part of the 1st Assignment for the Fundamentals of Data Science course.
Course: BSc (Hons) Computer Science - AI, Batch 2025, Level 3, Semester 2, Section H
This is a number guessing game where the player has to guess a randomly generated number within a specified range. 
The game provides feedback on how close the guess is and calculates a score based on the proximity of the guess to the target number. 
The player has  5 attempts to guess the number, and the score is adjusted based on how close he guessed and in which attempt he guessed it correctly.'''


import random #to generate random numbers
import os #to clear the screen
import sys #to print to the console
import time #to add delay in printing

#Constants for scoring
improvementMultiplier = 2
penaltyMultiplier = 3
repeatGuessPenalty = 10.0 


def clearScreen():  #function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def slowPrint(text, delay=0.05): #function to print text slowly
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def instructions():  #function to display instructions in instructions page
    clearScreen()
    print("--------Instructions--------")
    print("1. Choose a difficulty level.")
    print("2. Guess the number within the range.")
    print("3. You have 5 attempts.")
    print("4. Score is based on how close your guess is to the number (percentile-based).")
    input("Press Enter to return to main menu...")


def credits(): #function to display credits in credits section
    clearScreen()
    slowPrint("Game developed by Pragyan Timalsina.")
    slowPrint("1st Assignment - Fundamentals of Data Science.")
    slowPrint("Guided by Mr. Surav Gautam.")
    slowPrint("BSc (Hons) Computer Science - AI, Batch 2025, Level 3, Semester 2")
    slowPrint("The British College, Kathmandu")
    input("Press Enter to return to main menu...")


def difficultyRange(choice): #function to set the range of numbers based on difficulty level (easy to extreme)
    ranges = { #dictionary to set the range of numbers
        1: (-100, 100),
        2: (-500, 500),
        3: (-1000, 1000),
        4: (-10000, 10000)
    }
    return ranges.get(choice)


def calculateProximity(guess, target, range_min, range_max): #function to calculate the proximity of the guess to the target number
    guess_pct = (guess - range_min) / (range_max - range_min) * 100  
    target_pct = (target - range_min) / (range_max - range_min) * 100
    return abs(guess_pct - target_pct) 


def feedbackMessage(proximity): #function to provide feedback based on the proximity of the guess to the target number
    if proximity == 0:
        return "Correct! You've guessed the number."
    elif proximity <= 5:
        return "Your guess is in the top 5%"
    elif proximity <= 10:
        return "Your guess is in the top 10%"
    elif proximity <= 20:
        return "Your guess is in the top 20%"
    elif proximity <= 30:
        return "Your guess is in the top 30%"
    elif proximity <= 40:
        return "Your guess is in the top 40%"
    elif proximity <= 50:
        return "Your guess is in the top 50%"
    elif proximity <= 60:
        return "Your guess is in the top 60%"
    elif proximity <= 70:
        return "Your guess is in the top 70%"
    elif proximity <= 80:
        return "Your guess is in the top 80%"
    elif proximity <= 90:
        return "Your guess is in the top 90%"
    elif proximity <= 95:
        return "Your guess is in the top 95%"
    else:
        return "Your guess is in the lower 5%"


def validInput(prompt, expected_type=int, valid_range=None): #function to validate the input from the user
    while True:
        try:
            value = expected_type(input(prompt))
            if valid_range and value not in valid_range:
                print(f"Please choose a valid option: {valid_range}")
                continue
            return value
        except ValueError:
            print(f"Please enter a valid {expected_type.__name__}.")


def gameStart(): #function to start the game
    clearScreen()
    print("--------Number Guesser--------")
    input("Press Enter to start...")
    clearScreen()
    # Main game loop
    while True: 
        print("Select Difficulty:")
        print("1. Easy (-100 to 100)")
        print("2. Medium (-500 to 500)")
        print("3. Hard (-1000 to 1000)")
        print("4. Extreme (-10000 to 10000)")
        print("5. Return to Main Menu")
        
        # Get user input for difficulty level
        difficulty = validInput("Your choice (1-5): ", int, range(1, 6))
        clearScreen()

        # Exit the game if the user chooses to return to the main menu
        if difficulty == 5:
            break
        
        # Set the range of numbers based on difficulty level
        rangeMin, rangeMax = difficultyRange(difficulty)
        targetNumber = random.randint(rangeMin, rangeMax)
        maxAttempts = 5
        currentScore = 0.0

        # Initialize variables for tracking guesses and scores
        previousProximity = None
        previousGuesses = set()
        playerGuesses = []
        score_by_attempt = [100.0, 90.0, 70.0, 60.0, 50.0]
        
        # Game loop for guessing
        for attempt in range(1, maxAttempts + 1):
            print(f"Attempt {attempt} of {maxAttempts}") 
            print(f"Current Score: {currentScore:.2f}")
            guess = validInput(f"Guess the number ({rangeMin} to {rangeMax}): ")

            if guess < rangeMin or guess > rangeMax: # Check if guess is within range
                print(f"Guess must be between {rangeMin} and {rangeMax}.")
                continue
            
            # Check for repeated guesses
            if guess in previousGuesses:
                print(f"Repeated guess detected. Penalty of {repeatGuessPenalty:.2f} points.")
                currentScore -= repeatGuessPenalty
                currentScore = round(max(0.0, min(100.0, currentScore)), 2)  # Ensure score is within bounds
                continue
            
            previousGuesses.add(guess) # Add guess to previous guesses
            playerGuesses.append(guess) 
            
            # Calculate proximity and provide feedback
            proximity = calculateProximity(guess, targetNumber, rangeMin, rangeMax)
            feedback = feedbackMessage(proximity)
            print(feedback)

            # If correct guess
            if guess == targetNumber:
                clearScreen()
                currentScore += round(score_by_attempt[attempt - 1], 2) #adds the score of the attempt to the current score
                print(f"\nCorrect! You got it in attempt {attempt}. Score: {currentScore:.2f}")
                break

            # If incorrect guess, calculate score based on proximity
            if previousProximity is None:
                scoreThisRound = round(100.0 - proximity, 2)*0.1
                print(f"  Your first guess! Score: +{scoreThisRound:.2f} points")
                currentScore += scoreThisRound
            else: # Calculate score based on proximity change
                proximityDelta = previousProximity - proximity
                scoreThisRound = (score_by_attempt[attempt - 1])*0.1

                if proximityDelta > 0: # Closer to the target number
                    gain = round((proximityDelta / 100) * scoreThisRound, 2)
                    print(f"You're closer! +{gain:.2f} points.")
                    currentScore += gain
                elif proximityDelta < 0: # Further from the target number
                    loss = round((abs(proximityDelta) / 100) * scoreThisRound, 2)
                    print(f"You got further away. -{loss:.2f} points.")
                    currentScore -= loss
                else:
                    print("Same proximity. No score change.")

            # Ensure score is within bounds
            currentScore = round(max(0.0, min(100.0, currentScore)), 2) 
            previousProximity = proximity

            input("Press Enter for next attempt...")
            clearScreen()

        # End of game summary
        print("\nNumbers you guessed:", ', '.join(str(g) for g in playerGuesses))
        print(f"\nThe number was: {targetNumber}")
        print(f"Your final score: {currentScore:.2f}/100")

        # Provide feedback based on final score
        if currentScore == 100.0:
            print("Perfect! Well done!")
        elif currentScore >= 90.0:
            print("Excellent work!")
        elif currentScore >= 80.0:
            print("Great job!")
        elif currentScore >= 70.0:
            print("Good effort!")
        elif currentScore >= 60.0:
            print("Room for improvement.")
        elif currentScore >= 50.0:
            print("Not bad, keep improving!")
        else:
            print("Try again and aim higher!")

        # Ask if the player wants to play again
        playAgain = input("\nPlay again? (y/n): ").strip().lower()
        if playAgain != 'y':
            break
        clearScreen()

# Main function to run the game
def main():
    while True: # Main menu loop
        clearScreen()
        print("--------Number Guesser--------")
        print("1. Play Game")
        print("2. Instructions")
        print("3. Credits")
        print("4. Exit")

        # Get user input for menu choice
        choice = validInput("Choose an option (1-4): ", int, range(1, 5))
        
        if choice == 1:
            gameStart()
            clearScreen()
        elif choice == 2:
            instructions()
        elif choice == 3:
            credits()
        elif choice == 4:
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__": # Entry point of the program 
    main()
