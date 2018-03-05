class Room(******):
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
your_house = Room("YOUR HOUSE", None, "your_car_outside", "neighbors", None, None, None,
                  "Welcome, the day has come, the undead rule the world but, you can make a difference by finding a "
                  "cure. East is where your neighbors live, and South is your car, broken because of all the anarchy.")
your_car_outside = Room("OUTSIDE OF CAR", "your_house", None, "joe's_burgers", None, "inside_of_car", None,
                "The door is open, missing its window, the engine is missing, which probably means everything inside "
                "is stolen.")
your_car_inside = Room("INSIDE OF CAR", None, None, None, None, None, "your_car_outside",
                       "Nothing much, just window shards, and a pen on what looks like to be your bloody car mat.")
joes_burger_outside = Room("OUTSIDE JOE'S BURGERS", "neighbors", "parking_lot", None, "your_car_outside", None, None,
                           "One of the best fast food place, Joe's Burgers with extra calories and fat.")
neighbors = Room("YOUR NEIGHBORS INSIDE", )

current_node = Hazardine_City["YOUR HOUSE"]
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
            name_of_code = current_node['PATHS'][command]
            current_node = Hazardine_City[name_of_code]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()