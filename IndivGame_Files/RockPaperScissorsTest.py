import random

#Create While True loop to allow user to play multiple times
while True:
    #Track user input
    userAction = input("Enter a choice (rock, paper, or scissors): ")
    possibleActions = ["rock", "paper", "scissors"] #Store options

    #This makes the computer actiosn be randomized to choose either 3 choices
    computerAction = random.choice(possibleActions)

    print(f"\nYou chose {userAction}, computer chose {computerAction}.\n")

    #If statements to test the possible outcomes of the game based on choices
    #f in the print option is to indicate that variables inside curly bracket are to replace imported values

    if userAction == computerAction:
        print(f"Both players selected {userAction}. It's a tie!")
    # elif is else if
    elif userAction == "rock":
        if computerAction == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userAction == "paper":
        if computerAction == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userAction == "scissors":
        if computerAction == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    #This askes the user to play again, y or n if no, it ends, if yes, it restarts
    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        break
