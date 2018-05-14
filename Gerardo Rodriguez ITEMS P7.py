inventory1 = []


class Character(object):
    def __init__(self, take_damage, stamina, fight, inventory, health, damage):
        self.takeDamage = take_damage
        self.stamina = stamina
        self.fight = fight
        self.inventory = inventory
        self.health = health
        self.damage = damage

    def fight(self):
        if self.stamina >= 10:
            print("You kick the zombie.")
            self.stamina -= 10

        if self.stamina <= 60:
            print("You should run.")

        if self.health <= 60:
            print("You should run.")

    def block(self):
        if self.health >= 20:
            print("You block but you can feel the pain.")
            self.health -= 20

        if self.health <= 60:
            print("You should run.")

        if self.stamina <= 60:
            print("You should run.")


character = Character("take_damage", "stamina", "fight", "inventory", 100, "damage")


class Item(object):

    def __init__(self, name, description, use, heal):
        self.name = name
        self.description = description
        self.use = use
        self.heal = heal


class Healing(Item):

    def __init__(self, name, description, use, heal):
        super(Healing, self).__init__(name, description, use, heal)
        self.name = name
        self.description = description
        self.use = use
        self.heal = heal

        def heal(self):
            if Burger or Soda or Enchancer in inventory1:
                self.heal += Character.health


class Burger(Healing):
    def __init__(self, name, description, use, heal):
        super(Burger, self).__init__(name, description, use, heal)

        def heal(self):
            if Burger in inventory1:
                print("I would suggest to eat this delicious burger even though I doubt you have an appetite.")
                self.heal += Character.health


class Soda(Healing):
    def __init__(self, name, description, use, heal):
        super(Soda, self).__init__(name, description, use, heal)

        def heal(self):
            if Soda in inventory1:
                print("Nothing better than a nice soda.")
                self.heal += Character.health


class Enchancer(Healing):
    def __init__(self, name, description, use, heal):
        super(Enchancer, self).__init__(name, description, use, heal)

        def heal(self):
            if Enchancer in inventory1:
                print("This bad boy can heal or add extra health.")
                self.heal += Character.health


class Armour(Item):
    def __init__(self, name, description, use, durability):
        super(Armour, self).__init__(name, description, use, durability)
        self.name = name
        self.description = description
        self.use = use
        self.durability = durability

        def protection(self):
            if Mask or ChestPlate or IronFists in inventory1:
                self.durability += Character.health


class Mask(Armour):
    def __init__(self, name, description, use, durability):
        super(Armour, self).__init__(name, description, use, durability)
        self.name = name
        self.description = description
        self.use = use
        self.durability = durability

        def protection(self):
            if Mask in inventory1:
                self.durability += Character.health


class ChestPlate(Armour):
    def __init__(self, name, description, use, durability):
        super(Armour, self).__init__(name, description, use, durability)
        self.name = name
        self.description = description
        self.use = use
        self.durability = durability

        def protection(self):
            if ChestPlate in inventory1:
                self.durability += Character.health


class IronFists(Armour):
    def __init__(self, name, description, use, durability):
        super(Armour, self).__init__(name, description, use, durability)
        self.name = name
        self.description = description
        self.use = use
        self.durability = durability

        def protection(self):
            if IronFists in inventory1:
                self.durability += Character.health


class Weapon(Item):
    def __init__(self, name, description, use, damage):
        super(Weapon, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def damage(self):
            if Pistol or Shotgun or SMG or M14 or AK12 or Knife or BaseballBat in inventory1:
                self.damage += Character.damage


class Pistol(Item):
    def __init__(self, name, description, use, damage):
        super(Pistol, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if Pistol in inventory1:
                self.damage += Character.damage


class Shotgun(Item):
    def __init__(self, name, description, use, damage):
        super(Shotgun, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if Shotgun in inventory1:
                self.damage += Character.damage


class SMG(Item):
    def __init__(self, name, description, use, damage):
        super(SMG, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if SMG in inventory1:
                self.damage += Character.damage


class M14(Item):
    def __init__(self, name, description, use, damage):
        super(M14, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if M14 in inventory1:
                self.damage += Character.damage


class AK12(Item):
    def __init__(self, name, description, use, damage):
        super(AK12, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if AK12 in inventory1:
                self.damage += Character.damage


class Knife(Item):
    def __init__(self, name, description, use, damage):
        super(Knife, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if Knife in inventory1:
                self.damage += Character.damage


class BaseballBat(Item):
    def __init__(self, name, description, use, damage):
        super(BaseballBat, self).__init__(name, description, use, damage)
        self.name = name
        self.description = description
        self.use = use
        self.damage = damage

        def Damage(self):
            if BaseballBat in inventory1:
                self.damage += Character.damage

