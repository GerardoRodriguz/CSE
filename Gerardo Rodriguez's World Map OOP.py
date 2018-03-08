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
joes_burgers_inside = Room("INSIDE JOE'S BURGERS", "cashier_back", None, None, "your_car_outside", None, None, "Wow. "
                    "Tables are all flipped over and on the floor is mustard, ketchup, soda, and not sure if on the "
                    "floor is blood but cannot notice because of all the condiments and soda. It is weird how this is "
                                    "a burger place but there is no burgers on the floor or still standing tables...")
cashier_back_joes_burgers = Room("CASHIER BACK", "parking_lot", "joes_burgers_inside", None, None, None, "exit", "Shh... "
                          "there is a mess full of raw meat, blood, and two weird human-like creatures. Why not "
                          "say human? Mostly since they were all bloody, ripped clothes, and the fact they are eating "
                                                                                  "frozen beef, chicken, and raw meat.")
jims_house_outside = Room("OUTSIDE OF JIM'S HOUSE", None, "joes_burgers_outside", "your_house", "gas_stop",
                          "jims_house_inside", None, "This is your neighbor's house, he was a quiet neighbor and to "
                          "say the truth, he was creepy. His house looks all messed up because of anarchy and the "
                                                     "door is wide open. Strange..." )
jims_house_inside = Room("INSIDE OF JIM'S HOUSE", "jims_bathroom", "jims_bedroom", "gas_stop", "your_house", None,
                         "your_house", "Looks like someone already looted the place, only a table with a missing leg "
                         "remains with the furniture. North is Jim's bathroom, South is Jim's bedroom, East is an "
                                       "exit, and another exit behind you.")

jims_bathroom =
current_node = your_house
directions = ["north", "south", "east", "west", "inside", "outside"]
short_directions = ["n", "s", "e", "w", "i", "o"]

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_ ').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos  = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            name_of_code = current_node["directions"][command]
            current_node = your_house[name_of_code]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()