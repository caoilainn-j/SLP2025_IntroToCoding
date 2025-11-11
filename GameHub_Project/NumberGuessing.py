import random
import os

def number_guessing_game():
    correct_number = random.randint(1, 100)
    guess = 0
    attempts = 0
    input("\nPress enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 & 100. What is it?")

    while guess != correct_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < correct_number:
                print("Too low, try again.")
            elif guess > correct_number:
                print("Too high, try again.")
            else:
                print(f"\n Congratulations! You guessed the number {correct_number} correctly!")
                print(f"It took you {attempts} attempts.")

                input("\nPress enter to continue...")

        except:
            print("Invalid input. Please enter a whole number.")