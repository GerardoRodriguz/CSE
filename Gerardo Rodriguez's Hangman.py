import random
"""
Outline of Hangman
1.Make a word bank - 10 items
2.Select a random item from the list
3.Add user input to list of letters_guessed
4.Build a list of letters to show, and display the string form
5.Create the win condition

"""

letter = ("a", "b", "c", "d", "e", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
          "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
          "U", "V", "W", "X", "Y", "Z")
letters_guessed = []
words = ["Smoke", "Thermite", "Jackal", "Valkyrie", "IQ", "Rook", "Sledge", "Bandit", "Twitch", "Blitz"]
guesses = 0
print(random.choice(words))


while int(letter) != letter and words:
    guess = input("What is your guess?")
    if letter != letter and words:
        print("Wrong")
    if letter == letter and words:
        print("Correct!")
if guesses >= 0-8:
    print("Hangman was made.")

print()