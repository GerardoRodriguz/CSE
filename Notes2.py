# print("Hello World")
'''





# print(3**2)

# print()  # Creates a blank line
# print("See if you can figure this out")
# print(15%5)
#
# Varibles
# car_name = "Wiebe Mobile"
# car_type = "Lamborghini Sesto Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
#  Inline Printing
# print("My car is the ")


# Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# print(name)

# age = input("How old are you")
# print("%s? You are young")

 # Change to the file


# def print_hw():
#     print("Hello World")


# print_hw()


# def say_hi(name):  # name is a "parameter"
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day.")
#
#
# say_hi("John")
#
#
# def birthday(age):
#     age = age + 1  # age = age + 1
#     print(age)
#
#
# def say_hi(John):
#     print("John is 15. Next year:")
#     birthday(15)
# birthday(15)
#
# Press Ctrl-A and Ctrl-/
# to comment old code


# def f(x):
#     return x**5 + 4 * x **4 - 17*x**2 + 4
#
#
# print(f(3))
# print(f(3) + f(5))
#
# If statements


# def grade_cala(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80: # Else if
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage >= 0: #else:
#         return "F"

# Loops
# for num in range(5):
#     print(num + 1)



# for mystery in "Hello World":
#     print(mystery)

# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# response = ""
# while response != "Hello":
#     response = input("Say \\ \"Hello\"")
#
# print("Hello \nWorld") # \n means newline
#
# import random  # imports should be at the top
# print(random.randint(0, 6))

# Comparisons
# print(1 == 1) # Two equal signs to compare
# print(1 != 2) # One is not equal to 2
# print(not False) # This prints true
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5 > 1) # True
#
# Recasting
# c = "1"
# print(c == 1) # False - c is a string, 1 is an int
# print(int(c) == 1) # True - Compare two ints
# print(c == str(1)) # True - Compare two strings
#
#
# num = input("Give me a number")
# Inputs are ALWAYS (!!!!!!!) of type string!!!
# 12/5/17


# Lists

the_count = [1, 2, 3, 4, 5]
characters = ["Graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
print(characters[0])
print(characters[4])

print(len(characters))  # Gives you the length of the list

# Going through lists
for char in characters:
    print(char)

for num in the_count:
    # print(num)
    print(num ** 2)

len(characters)
range(3)   # Makes a list of the numbers from 0 to 2
range(len(characters))  # Makes a list of ALL INDICES

for num in range(len(characters)):
    char = characters[num]
    print("The character at the index %s" % (num, char))

str1 = "Hello World"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
newStr = "".join(listOne)
print(newStr)
print(listOne[100])

# adding stuff to a list
characters.append("Ironman/Batman/whomever you want")
print(characters)

characters.append("Spider-man")

# Removing things from a list
characters.remove("Carl")
print(characters)

characters.pop(6)
print(characters)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)

strTwo = 'ThIs sEntENce iS uNuSuAL'
lowercase = strTwo.lower()
print(lowercase)
'''

# Dictionaries - Make up a key: value pair
dictionary = {"name": "Lance", "age": 18, "height": 6 * 12 + 2}

# Accessing from a dictionary
print(dictionary["name"])
print(dictionary["height"])
print(dictionary["age"])

# Adding to a dictionary
dictionary["eye colour"] = "blue"
dictionary["toilet towels"] = True
print(dictionary)

large_dictionary = {
    "California": "CA",
    "Michigan": "MI",
    "Florida": "FL"
}
print(large_dictionary["Florida"])

larger_dictionary = {
    "California": [
        "Fresno",
        "Sacremento",
        "Los Angles"
    ]
}
#
# print(larger_dictionary["Illinois"])
# print(larger_dictionary["Illinois"][0])
# print(larger_dictionary["Illinois"][])

largest_dictionary = {
    "CA": {
        "NAME": "California",
        "Population": 39250000,
        "BORDER ST": [
             "Oregon",
             "Nevada",
             "Arizona"
         ]
     },
    "MI": {
        "NAME": "Michigan",
        "POPULATION": 9928000,
        "BORDER ST": [
            "Wisconsin",
            "Ohio",
            "Indiana"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 20610000,
        "BORDER ST": [
            "Georgia",
            "Alabama"
        ]
    }
}

print(largest_dictionary["FL"]["Border ST"][1])  # Get this to print out Ohio.






