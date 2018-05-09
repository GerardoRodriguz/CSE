import random

# import statements (you may not have any)
# class definitions
# items
# characters
# rooms
# instantiation of classes
# controller

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


# west_house = Room("West of House, 'north house")
# north_house = Room("North of House", None)

your_house = Room("YOUR HOUSE", None, "your_car_outside", "jims_house_outside", None, None, None,
                  "Welcome, the day has come, the undead rule the world but, you can make a difference by finding a "
                  "cure. East is where your neighbors live, and South is your car, broken because of all the anarchy.")
your_car_outside = Room("OUTSIDE OF CAR", "your_house", "kates_house", "joe's_burgers", None, "inside_of_car", None,
                "The door is open, missing its window, the engine is missing, which probably means everything inside "
                "is stolen.")
your_car_inside = Room("INSIDE OF CAR", None, None, None, None, None, "your_car_outside",
                       "Nothing much, just window shards, and a pen on what looks like to be your bloody car mat.")
joes_burgers_outside = Room("OUTSIDE JOE'S BURGERS", "jims_house_outside", "parking_lot", None, "your_car_outside",
                            "joes_burgers_inside", "joes_burgers_outside","One of the best fast food place, Joe's "
                                                                          "Burgers with extra calories and fat.")
joes_burgers_inside = Room("INSIDE JOE'S BURGERS", None, "cashier_back_joes_burgers", None, "your_car_outside", None,
                           "joes_burgers_outside", "Wow. "
                    "Tables are all flipped over and on the floor is mustard, ketchup, soda, and not sure if on the "
                    "floor is blood but cannot notice because of all the condiments and soda. It is weird how this is "
                                    "a burger place but there is no burgers on the floor or still standing tables...")
cashier_back_joes_burgers = Room("CASHIER BACK", "joes_burgers_inside", "parking_lot", None, None, None,
                            "parking_lot", "Shh... there is a mess full of raw meat, blood, and two weird "
                            "human-like creatures. Why not say human? Mostly since they were all bloody, "
                            "ripped clothes, and the fact they are eating frozen beef, chicken, and raw meat.")
jims_house_outside = Room("OUTSIDE OF JIM'S HOUSE", None, "joes_burgers_outside", "your_house", "gas_stop_outside",
                          "jims_house_inside", None, "This is your neighbor's house, he was a quiet neighbor and to "
                          "say the truth, he was creepy. His house looks all messed up because of anarchy and the "
                                                     "door is wide open. Strange...")
jims_house_inside = Room("INSIDE OF JIM'S HOUSE", "jims_bathroom", "jims_bedroom", "gas_stop_outside",
                         "your_house", None,
                         "your_house", "Looks like someone already looted the place, only a table with a missing leg "
                         "remains with the furniture. North is Jim's bathroom, South is Jim's bedroom, East is an "
                                       "exit, and another exit behind you.")

jims_bathroom = Room("JIM'S BATHROOM", None, "jims_house_inside", None, None, None, "jims_house_inside", "Jim clearly "
                     "does not clean his bathroom at all. But besides that, everything is gone except the toilet, "
                                                                                                  "sink, and bathroom.")
jims_bedroom = Room("JIM'S BEDROOM", "jims_house_inside", None, None, None, None, "jims_house_inside", "It looks like "
                    "a massacre in here with all the bedsheets covered up in a blood and there seems to be a "
                    "figure standing there just staring at a wall. I would recommend to leave.")
kates_house_outside = Room("OUTSIDE KATE'S HOUSE", "your_car", None, "parking_lot", None, "kates_house_inside",
                      None, "Kate, Kate, Kate, she was ex before al this and with all this happening, I wonder where "
                      "she is. To shorten the history between you and your ex, you guys only separated because of "
                            "the universities. You haven't had the guts to pass by her house at all...")
kates_house_inside = Room("INSIDE KATE'S HOUSE", "kates_house_outside", "kates_basement", "parking_lot",
                     "kates_kitchen", None, "kates_house_outside", "Well, considering the whole apocalypse, her house "
                     "is looking decent and mostly everything is in place. There seems to be some stairs leading "
                     "down South, East is a door exit, and West is Kate's kitchen. I keep getting a strange "
                                                                   "feeling someone is in this house...")
kates_basement = Room("KATE'S BASEMENT", "kates_house_inside", None, None, None, None, "kates_basement", "You see "
                 "very little but you can see visible a creature, this is creepy.")
kates_kitchen = Room("KATE'S KITCHEN", None, None, "kates_house_inside", None, None, "kates_house_inside",
                "Nevermind, looks like the house isn't alone after all if you consider a creature eating raw meat from "
                "a fridge. Slowly move out of this room. You know, if you want to live.")
gas_stop_outside = Room("OUTSIDE GAS STOP", None, "mall_outside", None, "jims_house_outside", "gas_stop_inside", None,
                   "If you had a vehicle with low gas, this would be the perfect place to go to but for a snack, not "
                                "so much if you consider blood dripping from the main entrance.")
gas_stop_inside = Room("INSIDE GAS STOP", None, "mall_outside", None, "gas_stop_outside", None, "gas_stop_outside",
                       "The aisles are all empty and there is a weird grunting sound coming from the left aisle. Maybe "
                                                                    "turn South to the exit to a store, I think.")
mall_outside = Room("OUTSIDE OF MALL", "gas_stop_outside", None, None, "parking_lot", "mall_inside", None, "Oh "
               "crude, this is a mall. Probably the worst place to go to in a zombie apocalypse and has been proven "
               "in many theories. You should be very quiet if you enter you know, if you want...we don't have to "
                                                                                                           "go right?")
mall_inside = Room("INSIDE OF MALL", "malls_shoe_store", None, "malls_food_court", "mall_outside", None,
              "mall_outside", "Ok, be carefull where you step and how you step, don't attract to much attention "
              "to yourself. North is the shoes store, South seems to be locked and unavailable, and East is the "
                              "breeding ground of these creatures, the food court.")
malls_shoe_store = Room("MALL'S SHOE STORE", None, "mall_inside", None, None, None, "mall_inside", "Even though "
                   "those Jordans look really fresh, maybe stick to your shoes because those your wearing look way "
                                            "less bulkier than those fresh Jordans. Just saying.")
mall_food_court = Room("MALL FOOD COURT", None, None, None, "mall_inside", None, "mall_inside", "Eyes are looking "
                                                "right at you, like dozens. Leave now because I really enjoy life.")
parking_lot = Room("PARKING LOT", "cashier_back_joes_burgers", None, "mall_outside", "kates_house_outside", None,
                   None, "Just any normal parking lot, empty and blood and guts on the floor.")
current_node = your_house
directions = ["north", "south", "east", "west", "inside", "outside"]
short_directions = ["n", "s", "e", "w", "i", "o"]


class Character(object):
    def __init__(self, take_damage, stamina, fight, inventory, health):
        self.takeDamage = take_damage
        self.stamina = 100
        self.fight = fight
        self.inventory = inventory
        self.health = 100

    def attack(self):
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


character = Character("take_damage", "stamina", "fight", "inventory", "health")


class Walker(Character):
    def __init__(self,  take_damage, stamina, fight, inventory, health, alerted, level, damage, attack):
        super(Walker, self).__init__( take_damage, stamina, fight, inventory, health)
        self.alerted = False
        self.level = 1
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

    def no_longer_notice(self):
        if self.alert:
            self.alert = False
            print("The Walker is no longer hostile.")
        else:
            print("The Walker seems to not notice.")

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



while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_ ').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos  = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()
