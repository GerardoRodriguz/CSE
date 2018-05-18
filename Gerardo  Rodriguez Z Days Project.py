class Item(object):
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use
        # self.heal = heal
        # self.damage = damage
        # self..durability = durability


class Healing(Item):
    def __init__(self, name, description, use, heal):
        super(Healing, self).__init__(name, description, use)
        self.heal = heal

    def heal(self):
        if Burger or Soda or Enhancer in inventory1:
            self.heal += MainCharacter.health


class Burger(Healing):
    def __init__(self, name, description, heal):
        super(Burger, self).__init__(name, description, "use", heal)

    def heal(self):
        if Burger in inventory1:
            print("I would suggest to eat this delicious burger even though I doubt you have an appetite.")
            self.heal += MainCharacter.health


class Soda(Healing):
    def __init__(self, name, description, heal):
        super(Soda, self).__init__(name, description, 'use', heal)

    def heal(self):
        if Soda in inventory1:
            print("Nothing better than a nice soda.")
            self.heal += MainCharacter.health


class Enhancer(Healing):
    def __init__(self, name, description, heal):
        super(Enhancer, self).__init__(name, description, 'use', heal)

    def heal(self):
        if Enhancer in inventory1:
            print("Would save it but...")
            self.heal += MainCharacter.health


class Armour(Item):
    def __init__(self, name, description, use, durability):
        super(Armour, self).__init__(name, description, use)
        self.durability = durability

    def protection(self):
        if Mask or ChestPlate or IronFists in inventory1:
            self.durability += MainCharacter.health


class Mask(Armour):
    def __init__(self, name, description, durability):
        super(Mask, self).__init__(name, description, 'use', durability)

    def protection(self):
        if Mask in inventory1:
            print("Cool, really like th fact that it protects your face from being ripped off but the design is nice..."
                  "")
            self.durability += MainCharacter.health


class ChestPlate(Armour):
    def __init__(self, name, description, durability):
        super(ChestPlate, self).__init__(name, description, 'use', durability)

    def protection(self):
        if ChestPlate in inventory1:
            print("Now were talking, this baby can stop those gnarly zombie teeth from ripping your flesh.")
            self.durability += MainCharacter.health


class IronFists(Armour):
    def __init__(self, name, description, durability):
        super(IronFists, self).__init__(name, description, 'use', durability)

    def protection(self):
        if IronFists in inventory1:
            print("Holy jesus, now your ready to smash some skulls.")
            self.durability += MainCharacter.health and MainCharacter.damage


class Weapon(Item):
    def __init__(self, name, description, use, damage):
        super(Weapon, self).__init__(name, description, use)
        self.damage = damage

    def damage(self):
        if DesertEagle or SPAS12 or UZI or M14 or AK12 or Knife or BaseballBat or BarrettM82 in inventory1:
            self.damage += MainCharacter.damage


class DesertEagle(Weapon):
    def __init__(self, name, description, damage):
        super(DesertEagle, self).__init__(name, description, 'use', damage)

    def damage(self):
        if DesertEagle in inventory1:
            print("Ok, this can be useful... for a while.")
            self.damage += MainCharacter.damage


class SPAS12(Weapon):
    def __init__(self, name, description, damage):
        super(SPAS12, self).__init__(name, description, 'use', damage)

    def damage(self):
        if SPAS12 in inventory1:
            print("This girl is a pump action, treat her well...")
            self.damage += MainCharacter.damage


class UZI(Weapon):
    def __init__(self, name, description, damage):
        super(UZI, self).__init__(name, description, 'use', damage)

    def damage(self):
        if UZI in inventory1:
            print("Too many pesky zombies, not anymore!")
            self.damage += MainCharacter.damage


class M14(Weapon):
    def __init__(self, name, description, damage):
        super(M14, self).__init__(name, description, 'use', damage)

    def damage(self):
        if M14 in inventory1:
            print("The standard military gun, this will be great.")
            self.damage += MainCharacter.damage


class AK12(Weapon):
    def __init__(self, name, description, damage):
        super(AK12, self).__init__(name, description, 'use', damage)

    def damage(self):
        if AK12 in inventory1:
            print("Just when the zombies to start having hope, this baby will DESTROY ALL HOPE!")
            self.damage += MainCharacter.damage


class BarrettM82(Weapon):
    def __init__(self, name, description, damage):
        super(BarrettM82, self).__init__(name, description, 'use', damage)

    def damage(self):
        if BarrettM82 in inventory1:
            print("One shot, one kill.")


class Knife(Weapon):
    def __init__(self, name, description, damage):
        super(Knife, self).__init__(name, description, 'use', damage)

    def damage(self):
        if Knife in inventory1:
            print("Welp, at least you can fight, sort of...")
            self.damage += MainCharacter.damage


class BaseballBat(Weapon):
    def __init__(self, name, description, damage):
        super(BaseballBat, self).__init__(name, description, 'use', damage)

    def damage(self):
        if BaseballBat in inventory1:
            print("OK, ok, not bad at all.")
            self.damage += MainCharacter.damage


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


character = Character("take_damage", "stamina", "fight", "inventory", "health", "damage")


class Walker(Character):
    def __init__(self,  take_damage, stamina, fight, inventory, health, level, damage, attack):
        super(Walker, self).__init__(take_damage, stamina, fight, inventory, health, damage)
        self.level = level
        self.damage = damage
        self.attack = attack
        self.health = health

    def attack_damage(self):
        if self.attack:
            self.damage -= 40
            print("You have been attacked by the Walker, you should run.")

    def strength(self):
        if self.level == 1:
            self.damage = 40
            self.health = 100

        elif self.level == 2:
            self.damage = 50
            self.health = 110

        elif self.level == 3:
            self.damage = 60
            self.health = 120


class MainCharacter(object):
    def __init__(self, take_damage, stamina, inventory, health, damage, max_health):
        self.takeDamage = take_damage
        self.stamina = stamina
        self.inventory = inventory
        self.health = health
        self.damage = damage
        self.max_health = max_health

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

    def take_damage(self, amount):
        self.health >= amount
            # print("ooooooffffff, just lost a bit of health, i would run.")


class Room(object):
    def __init__(self, name, north, south, east, west, inside, outside, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.inside = inside
        self.outside = outside
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


inventory1 = []


Burger = Burger("Burger", "I would suggest to eat this delicious burger even though I doubt you have an appetite.", 20)


Soda = Soda("Soda", "Nothing better than a nice soda.", 10)


Enhancer = Enhancer("Enhancer", "Would save it but...", 50)


BarrettM82 = BarrettM82("BarrettM82", "One shot, one kill.", 150)


M14 = M14("M14", "The standard military gun, this will be great.", 75)


AK12 = AK12("AK12", "Just when the zombies to start having hope, this baby will DESTROY ALL HOPE!", 90)


DesertEagle = DesertEagle("Desert Eagle", "Ok, this can be useful... for a while.", 25)


Knife = Knife("Knife", "Ok, this can be useful... for a while.", 10)


BaseballBat = BaseballBat("Baseball bat", "OK, ok, not bad at all.", 15)


UZI = UZI("UZI", "Too many pesky zombies, not anymore!", 35)


SPAS12 = SPAS12("SPAS-12", "This girl is a pump action, treat her well...", 55)


Mask = Mask("Mask", "Cool, really like th fact that it protects your face from being ripped off but the design is nice."
                    "..", 15)


IronFists = IronFists("Iron Fists", "Holy jesus, now your ready to smash some skulls.", 15)


ChestPlate = ChestPlate("Chest Plate", "Now were talking, this baby can stop those gnarly zombie teeth from ripping "
                                       "your flesh.", 30)


MainCharacter = MainCharacter("take_damage", 100, inventory1, 100, 10, 100)


# west_house = Room("West of House, 'north house")
# north_house = Room("North of House", None)
Walker = Walker("take_damage", "stamina", "fight", "inventory", "health", "level", "damage", "attack")


your_house = Room("YOUR HOUSE", None, "your_car_outside", "jim's_house_outside", None, None, None,
                  "Welcome, the day has come, the undead rule the world but, you can make a difference by finding a "
                  "cure. East is where your neighbors live, and South is your car, broken because of all the anarchy.")

your_car_outside = Room("OUTSIDE OF CAR", "your_house", "kate's_house", "joe's_burgers", None, "inside_of_car", None,
                        "The door is open, missing its window, the engine is missing, which probably means everything "
                        "inside is stolen.")

your_car_inside = Room("INSIDE OF CAR", None, None, None, None, None, "your_car_outside", "Nothing much, just window "
                       "shards, and a pen on what looks like to be your bloody car mat.")

joes_burgers_outside = Room("OUTSIDE JOE'S BURGERS", "jim's_house_outside", "parking_lot", None, "your_car_outside",
                            "joe's_burgers_inside", "joe's_burgers_outside", "One of the best fast food place, Joe's "
                            "Burgers with extra calories and fat.")

joes_burgers_inside = Room("INSIDE JOE'S BURGERS", None, "cashier_back_joe's_burgers", None, "your_car_outside", None,
                           "joe's_burgers_outside", "Wow. Tables are all flipped over and on the floor is mustard, "
                           "ketchup, soda, and not sure if on the floor is blood but cannot notice because of all the "
                           "condiments and soda. It is weird how this is a burger place but there is no burgers on the "
                           "floor or still standing tables...")

cashier_back_joes_burgers = Room("CASHIER BACK", "joe's_burgers_inside", "parking_lot", None, None, None,
                                 "parking_lot", "Shh... there is a mess full of raw meat, blood, and two weird "
                                 "human-like creatures. Why not say human? Mostly since they were all bloody, "
                                 "ripped clothes, and the fact they are eating frozen beef, chicken, and raw meat.")

jims_house_outside = Room("OUTSIDE OF JIM'S HOUSE", None, "joe's_burgers_outside", "your_house", "gas_stop_outside",
                          "jim's_house_inside", None, "This is your neighbor's house, he was a quiet neighbor and to "
                          "say the truth, he was creepy. His house looks all messed up because of anarchy and the "
                          "door is wide open. Strange...")

jims_house_inside = Room("INSIDE OF JIM'S HOUSE", "jim's_bathroom", "jim's_bedroom", "gas_stop_outside",
                         "your_house", None, "your_house", "Looks like someone already looted the place, only a table"
                         " with a missing leg remains with the furniture. North is Jim's bathroom, South is Jim's "
                         "bedroom, East is an exit, and another exit behind you.")

jims_bathroom = Room("JIM'S BATHROOM", None, "jim's_house_inside", None, None, None, "jim's_house_inside", "Jim clearly"
                     " does not clean his bathroom at all. But besides that, everything is gone except the toilet, sink"
                     ", and bathroom.")

jims_bedroom = Room("JIM'S BEDROOM", "jim's_house_inside", None, None, None, None, "jims_house_inside", "It looks like "
                    "a massacre in here with all the bedsheets covered up in a blood and there seems to be a "
                    "figure standing there just staring at a wall. I would recommend to leave.")

kates_house_outside = Room("OUTSIDE KATE'S HOUSE", "your_car", None, "parking_lot", None, "kates_house_inside", None,
                           "Kate, Kate, Kate, she was ex before al this and with all this happening, I wonder where "
                           "she is. To shorten the history between you and your ex, you guys only separated because of "
                           "the universities. You haven't had the guts to pass by her house at all...")

kates_house_inside = Room("INSIDE KATE'S HOUSE", "kate's_house_outside", "kate's_basement", "parking_lot",
                          "kate's_kitchen", None, "kates_house_outside", "Well, considering the whole apocalypse, her"
                          " house is looking decent and mostly everything is in place. There seems to be some stairs "
                          "leading down South, East is a door exit, and West is Kate's kitchen. I keep getting a "
                          "strange feeling someone is in this house...")

kates_basement = Room("KATE'S BASEMENT", "kate's_house_inside", None, None, None, None, "kate's_basement", "You see "
                      "very little but you can see visible a creature, this is creepy.")

kates_kitchen = Room("KATE'S KITCHEN", None, None, "kate's_house_inside", None, None, "kate's_house_inside", "Nevermore"
                     ", looks like the house isn't alone after all if you consider a creature eating raw meat from a "
                     "fridge. Slowly move out of this room. You know, if you want to live.")

gas_stop_outside = Room("OUTSIDE GAS STOP", None, "mall_outside", None, "jim's_house_outside", "gas_stop_inside", None,
                        "If you had a vehicle with low gas, this would be the perfect place to go to but for a snack, "
                        "not so much if you consider blood dripping from the main entrance.")

gas_stop_inside = Room("INSIDE GAS STOP", None, "mall_outside", None, "gas_stop_outside", None, "gas_stop_outside",
                       "The aisles are all empty and there is a weird grunting sound coming from the left aisle. Maybe "
                       "turn South to the exit to a store, I think.")

mall_outside = Room("OUTSIDE OF MALL", "gas_stop_outside", None, None, "parking_lot", "mall_inside", None, "Oh crude, "
                    "this is a mall. Probably the worst place to go to in a zombie apocalypse and has been proven in "
                    "many theories. You should be very quiet if you enter you know, if you want...we don't have to go "
                    "right?")

mall_inside = Room("INSIDE OF MALL", "malls_shoe_store", None, "malls_food_court", "mall_outside", None, "mall_outside",
                   "Ok, be careful where you step and how you step, don't attract to much attention to yourself. North "
                   "is the shoes store, South seems to be locked and unavailable, and East is the breeding ground of "
                   "these creatures, the food court.")

malls_shoe_store = Room("MALL'S SHOE STORE", None, "mall_inside", None, None, None, "mall_inside", "Even though those "
                        "Jordans look really fresh, maybe stick to your shoes because those your wearing look way less "
                        "bulkier than those fresh Jordan. Just saying.")

mall_food_court = Room("MALL FOOD COURT", None, None, None, "mall_inside", None, "mall_inside", "Eyes are looking "
                       "right at you, like dozens. Leave now because I really enjoy life.")

parking_lot = Room("PARKING LOT", "cashier_back_joes_burgers", None, "mall_outside", "kate's_house_outside", None,
                   None, "Just any normal parking lot, empty and blood and guts on the floor.")


current_node = your_house
directions = ["north", "south", "east", "west", "inside", "outside"]
short_directions = ["n", "s", "e", "w", "i", "o"]


while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_ ').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()
