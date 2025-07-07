'''a program that implements a simple card guessing game where the computer randomly selects a card (value and suit)
and the player then guesses the card's value and suit, based on the guess, the program provides visual feedback
and messages, ending the game after one attempt.'''

import random; 'importing for random card selection'

def card_guesser():
    # list of card values
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    # list of card suites
    card_suites = ['spade', 'heart', 'diamond', 'club']

    # a random choice of card
    card = [random.choice(card_values), random.choice(card_suites)]
    print(card)

    while True:
        # asking the user to guess
        user_input = input("Guess the card value and suit (e.g., ace spade): ").lower()
        user_guess = user_input.split()

        # only runs if the user enters valid answer
        if len(user_guess) == 2 and user_guess[0] in card_values and user_guess[1] in card_suites:

            # if both value and suit are correct
            if user_guess[0] == card[0] and user_guess[1] == card[1]:
                print("""
```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⢔⣶⣖⢂⢒⡐⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                         ******       ******
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⢊⠵⠒⣩⠟⠛⠙⠂⠀⠀⠉⠒⢤⣾⣖⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      **********   **********
⠀⠀⠀⠀⠀⣀⡤⠄⣀⠀⠀⠀⠀⠀⢀⠔⡡⠊⠀⠀⠀⠁⣀⣀⠀⠀⠀⠀⠀⠀⠈⠉⠻⡆⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                    ************* *************
⠀⠀⠀⢠⠋⠁⠀⠀⠈⠱⡄⠀⠀⡠⠃⡜⠀⠀⠀⠀⢀⣾⠗⠋⠛⢆⠀⠀⠀⣠⣤⣤⡄⠉⢢⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  *****************************
⠀⠀⠀⢼⠀⠀⠀⠀⠀⠀⠱⠀⢠⠃⢠⠃⠀⠀⠀⠀⢸⠋⣠⣤⡀⠘⡆⠀⢰⡿⠋⠉⠳⣄⠈⣆⠀⠐⡄⠀⠀⢀⠔⠂⠐⠲⢄⠀⠀⠀                 ******************************
⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⢀⢃⠆⠀⠀⠁⠀⠀⢄⣀⣹⠀⣷⣼⣿⠀⢻⠀⢿⣖⣹⣷⡀⠈⡆⠈⠀⠀⢰⡀⠰⠃⠀⠀⠀⠀⠀⡇⠀⠀                  *****************************
⠀⠀⠀⠀⠈⣆⠤⠤⠤⠤⠾⣼⡀⠀⠀⠀⠀⠀⢀⡀⠂⠙⠻⡓⠋⢀⡏⠀⠀⢿⢿⡽⠃⠀⡜⠀⠀⠀⠀⡇⡇⠀⠀⠀⠀⠀⡠⠁⠀⠀                   ***************************
⠀⠀⢀⠔⡩⠀⠀⠀⠀⠀⠀⠀⠉⠓⢄⠀⠀⠊⠁⠙⢕⠂⠀⠘⡖⠊⠀⠀⠀⠀⠑⡤⠔⠊⡉⠐⠀⠀⢀⣰⡼⠤⠤⠤⢄⣰⠁⠀⠀⠀                    ************************
⠀⡰⠁⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠈⣶⡤⣀⠀⠀⠀⠀⠀⠀⠀⠁⠠⣲⠖⠤⢠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠁⠢⡀⠀                       *********************
⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠛⠒⢧⡀⠀⠀⠀⠀⠘⣷⣀⠉⠑⠒⠂⠒⢐⣦⠖⠋⠀⠀⠀⡗⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀                        ******************
⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠸⣿⣷⣦⣤⣤⣤⣾⠇⠀⠀⠀⠀⡴⠛⠉⠀⠀⠀⠀⠉⠐⠂⠀⠀⠀⠀⢠                            ************
⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⣀⡀⢀⠞⢄⠀⠀⠀⠀⠀⠘⢾⣿⣻⣿⣿⡟⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸                              ********
⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢎⠀⠈⠢⡀⠀⠀⠀⠀⠈⠛⠿⠿⢛⠁⠀⠀⠀⠀⠈⢆⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈                                ****
⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠻⢤⡀⠈⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⢻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                  **
⠀⠀⠀⠉⠢⢄⡀⠀⠀⠀⠀⢀⡠⠔⠊⠀⠀⠀⠉⠓⠦⣀⣁⠀⠀⠀⠀⠀⢀⣀⠤⠒⠊⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠉⢉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠤⠤⠤⠤⠒⠊⠁⠀⠀⠀
```
                    """)
                print(f"You won! The card was {card[0]} of {card[1]}s.")
                break 

            # if only value or suit is correct
            elif user_guess[0] == card[0] or user_guess[1] == card[1]:
                print("""
                    *****************                                      
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
           ****                           ****
               ******               ******
                    *****************

""")
                # for the value
                if user_guess[0] == card[0]:
                    print(f"You guessed the value correctly! It is a {card[0]} but of {card[1]}.")
                else: # for the suite
                    print(f"You guessed the suite correctly! It is a {card[1]} but of value {card[0]}.")
                break

            # if none of the values is correct
            else:
                print("""
⠀⢀⣴⣾⣿⣿⣿⣷⣦⡄⠀⣴⣾⣿⣿⣿⣿⣶⣄⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⠛⣿⣿⣿⣿⣿⣿⣿⣿⡆
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠙⣿⣿⣿⣿⣿⣿⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⣿⣧⡈⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡇⢸⣿⣿⠟⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⢿⡿⠀⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
""")
                print("You lost!")

        # an error message if the input is invalid
        else:
            print("Please enter in a valid format (e.g., ace spade)")

card_guesser()