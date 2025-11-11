import tkinter as tk
import random

# root.mainloop()

# Words to choose from
words = ["python", "java", "computer", "programming", "calpoly"]

# Hangman pictures
hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

# Game variables
word = ""
guessed = []
mistakes = 0

# Pick a new random word
def choose_new_word():
    global word, guessed, mistakes
    word = random.choice(words)
    guessed = []
    mistakes = 0
    hangman_label.config(text=hangman_art[0])
    message.config(text="Guess a letter!")
    entry.config(state="normal")
    update_word_display()

# Create window
root = tk.Tk()
root.title("Hangman Game")

# Hangman picture
hangman_label = tk.Label(root, text="", font=("Courier", 14))
hangman_label.pack()

# Show blanks
word_display = tk.Label(root, font=("Arial", 24))
word_display.pack()
message = tk.Label(root, text="")
message.pack()

# Entry box
entry = tk.Entry(root, width=5, font=("Arial", 24))
entry.pack()

# Update blanks
def update_word_display():
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    word_display.config(text=display)

# Guess letter
def guess_letter():
    global mistakes
    
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message.config(text="Enter ONE letter!")
        return

    if letter in guessed:
        message.config(text="You already guessed that!")
        return

    guessed.append(letter)

    if letter in word:
        message.config(text="Correct!")
    else:
        mistakes += 1
        message.config(text="Wrong!")
        hangman_label.config(text=hangman_art[mistakes])

    update_word_display()

    # Win check
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
    if won:
        message.config(text="You WIN!")
        entry.config(state="disabled")

    # Lose check
    if mistakes == 6:
        message.config(text="You LOST! The word was: " + word)
        entry.config(state="disabled")

# Guess button
button = tk.Button(root, text="Guess", command=guess_letter)
button.pack()

#Restart
restart_button = tk.Button(root, text="Restart", command=choose_new_word)
restart_button.pack()
    


