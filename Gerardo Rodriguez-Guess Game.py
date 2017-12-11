import random
# GerardoRodriguez


print(random.randint(1, 50))
number = (random.randint(1, 50))
guess = "0"
guesses = 0

while int(guess) != number and guesses < 5:
    guess = input("What is your guess?")
    if guess == str(number):
        print("Correct.")
    elif (int(guess) >= number):
        print("Lower.")
        guesses += 1
    elif (int(guess) <= number):
        print("Higher.")
        guesses += 1
if guesses >= 5:
        print("Goodbye")



































 #  2.Get a number (input) from the user
 #  3.Compare number to input
 #  4.Add "Higher" or "Lower"
 #  5.Add 5 guesses
 #  1.Generate a random number
 #  "1" == 1 false
 #  Varible for guesses