import random

name = input("What is your name?")
print("Good luck," + name + "!（＾・ω・＾✿）")

words = [
    "blossom",
    "meadow",
    "fern",
    "pollen",
    "willow",
    "petal",
    "dew",
    "thistle",
    "grove",
    "vine",
    "sunbeam",
    "moss",
    "orchid"
]

word = random.choice(words)

print("\nGuess the characters... o.o")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("\nYou win! (˶' ꒳ '˶)")
        print("The word is: ",word)
        break
    
    print()
    guess = input("Guess a character: ")
    
    guesses += guess
        
    if guess not in word:
        turns -= 1
        print("Wrong... ㅠ︿ㅠ")
        print("You have", + turns, 'more guesses.')
        
        if turns == 0:
            print("You lose ( ;´ - `;)")
            print("The word was: ", word)    