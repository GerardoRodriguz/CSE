import random


print(random.randint(1, 6))
print(random.randint(1, 6))
max_money = 15
money = 15
rolls = 0
rounds = 0
while money > 0:
    die1 = (random.randint(1, 6))
    die2 = (random.randint(1, 6))
    die_total = die1 + die2
    if die_total == 7:
        rolls += 1
        money += 4
        print("Its your lucky day!")
        print("Your money %s" % money)
        if money >= max_money:
            max_money = money
            rounds = rolls
        elif die_total != 7:
            money -= 1
            rolls += 1
            print("Next time!")
            print("Your money %s" % money)
        if money == 0:
            print("Sorry your out of money!")
            print(rolls)
            if max_money < 15:
                print("Too bad...")
            elif max_money > 14:
                print("You should have stopped at round %s when you had $%s" % (rounds, max_money))