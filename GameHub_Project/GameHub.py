# file to be used to host a "game hub" that leads to multiple different games based on user input,
# is runnable as the main

import os # for clearing terminal screen 
# imports the other .py files corresponding to the individual games
from RockPaperScissors import *
from Hangman import *
from NumberGuessing import *

# used to call for the instructions on how to play the game the user requested from their respective .py files
def getInstructions(gameChoice):
    endloop = False
    while not endloop:
        ynChoice = input("Would you like to see the instructions for the game? (y/n): ")
        if (ynChoice == 'y' or ynChoice == 'Y'):
            if(gameChoice == '1'):
                RockPaperScissorsInstructions()
                endloop = True
            elif(gameChoice == '2'):
                HangmanInstructions()
                endloop = True
            elif(gameChoice == '3'):
                NumberGuessingInstructions()
                endloop = True
            else:
                print("Invalid game choice, please select again.")
        elif (ynChoice == 'n' or ynChoice == 'N'):
            input("\nPress enter to continue...")
            endloop = True
        else:
            print("Not a valid choice, please select y or n")



def main():
    # loop here enables the "keep asking" if a user puts in an input that doesn't match 1, 2, 3, or q (for quit)
    endLoop = False
    while not endLoop:
        # works as a "clear" function to make terminal output neater
        os.system('cls' if os.name == 'nt' else 'clear')

        print("""Please select from the following games:
        (1) Rock-Paper-Scissors
        (2) Hangman
        (3) Higher/Lower 
        (q) Quit Game Hub \n\n""")

        # variable that takes in user input to match to a possible selection
        choice = input("Your selection: ")

        if(choice == '1'):
            print("You chose Rock-Paper-Scissors!\n")
            getInstructions(choice)
            playRockPaperScissors()

        elif(choice == '2'):
            print("You chose Hangman!")
            getInstructions(choice)
            playHangman()

        elif(choice == '3'):
            print("You chose Number Guessing!")
            getInstructions(choice)
            playNumberGuessing()

        elif(choice == 'q' or choice == 'Q'):
            print("Thank you for using the Game Hub!")
            endLoop = True

        else:
            print("Sorry, you chose an invalid option, please try again!")
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()