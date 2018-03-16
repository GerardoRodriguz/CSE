import random
"""
Outline of Hangman
1.Make a word bank - 10 items
2.Select a random item from the list
3.Add user input to list of letters_guessed
4.Build a list of letters to show, and display the string form
5.Create the win condition

"""

rainbow_six_operators = ["Thermite", "Bliz", "Valkarie", "Doc", "Smoke", "Thacher", "Ela", "Lion", "Finka", "Bandit"]

guesses_left = 10
word = random.choice(Fav_Streamers)
letters_guessed = list(string.punctuation + " ")

output = []
while guesses_left > 0 and "".join(output) != word:
    output = []
    for letter in word:
        if letter.lower() in letters_guessed:
            output.append(letter)
        else:
            output.append("^")
    print("".join(output))
    if "".join(output) == word:
        print("Nice.")
        continue
    guess = input("Pick a letter.").lower()
    letters_guessed.append(guess)
    if guess not in word.lower():
        guesses_left -= 1
        print("You have %d guesses left" % guesses_left)
