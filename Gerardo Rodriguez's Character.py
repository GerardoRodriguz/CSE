# Name
# Description
# Dialogue?
# Inventory
# Interact
# Move?
# Climb
# Look
# Item
# Fight
# Health
# Take Damage
# Death
# Stats


class Character(object):
    def __init__(self, take_damage, stamina, fightORshoot, inventory, health):
        self.takeDamage = take_damage
        self.stamina = 100
        self.fightORshoot = fightORshoot
        self.inventory = inventory
        self.health = 100

    def attack(self):
        if self.stamina >= 10:
            print("You kick the zombie.")
            self.stamina -= 10

        else:
            print("You should run.")

    def block(self):
        if self.health >= 20:
            print("You block but you can feel the pain.")
            self.health -= 20
        else:
            print("You should run.")

character = Character("take_damage", "stamina", "fight", "inventory", "health")

class Walker(object):
    def __init__(self, color, health, status, alerted, level, damage, attack):
       self.color = color
       self.health = 100
       self.status = status
       self.alerted = False
       self.level = level
       self.damage = 40
       self.attack = attack


    def alert(self):
        if self.alerted:
            self.alerted = False
            print("The Walker seems to not notice.")
        else:
            print("The Walker is now alert.")
            self.alert = True


    def hostility(self):
        if self.alerted:
            print("The Walker attacks.")
        else:
            print("The Walker seems to not notice.")


    def NoLongerNotice(self):
        if self.alert:
            self.alert = False
            print("The Walker is no longer hostile.")
        else:
            print("The Walker seems to not notice.")

    def AttackDamage(self):
        if self.attack:
            self.damage -= 40
            print("You have been attacked by the Walker, you should run.")
        else:
            print()


walker = Walker("color", "size", "status", "alerted", "level", "damage", "attack")