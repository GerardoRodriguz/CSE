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
    def __init__(self, size, attack_stamina, level, inventory, health):
        self.size = size
        self. attack_stamina = 100
        self.level = level
        self.inventory = inventory
        self.health = health

    def attack(self):
        if self.attack_stamina:
            print("You kick the zombie and your stamina is now 60/100.")
        else:
            print("")
class Walker(object):
    def __init__(self, color, size, status, alerted, level):
       self.color = color
       self.size = size
       self.status = status
       self.alerted = False
       self.level = level

    def alert(self):
        if self.alerted:
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