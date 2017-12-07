# New python File: Warmups.py

# 12.4.17
# Write a Python function
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.


def reverse_order(first_name, last_name):
   # print("%s %s" % (last_name, first_name)
   print(last_name + " " + first_name)   # Concatenation


def reverse_order():
        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        print("%s %s" % (last_name, first_name))


"""Warmup #2
Write a function called "happy_bday"
that "sings" (prints)
the Happy Birthday Song

It must take one parameter called "name"
"""

def happy_bday(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear %s" % name)
    print("Happy Birthday to you!")

# 12.5.17
"""Write a function called add_py
that takes one parameter called "name"
and prints out name.py
example:
add_py("I_ate_some") == "I_ate_some.py"
"""

def add_py(name):
    print("%s.py" % name) #Solution 1
    print(name + ".py") # Solution 2


# 12.6.17
"""Write a function called "add"
which takes three parameters
and prints the sum of the numbers
"""


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(90, 900, 9000)

# 12.7.17
# Write a function called "repeat"
# that takes one parameter (string)
# and prints it three times
#
# example:
# repeat("Hello") prints:
# Hello
# Hello
# Hello


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)