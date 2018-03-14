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
    def __init__(self, takeDamage, stamina, fight, inventory, health):
        self.takeDamage = takeDamage
        self.stamina = 100
        self.fight = fight
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

    def backpackSpace(self):
        if self.inventory
class Walker(object):
    def __init__(self, color, size, status, alerted, level):
       self.color = color
       self.size = size
       self.status = status
       self.alerted = False
       self.level = level

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