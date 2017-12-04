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
