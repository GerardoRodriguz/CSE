Hazardine_City = {
    "YOUR HOUSE": {
        "NAME": "YOUR HOUSE",
        "DESCRIPTION": "Welcome, the day has come, the undead rule the world but, you can make a difference by "
                       "finding a cure. East is where your neighbors live, and South is your car, broken because of "
                       "all the anarchy.",
        "PATHS": {
            "EAST": "NEIGHBORS",
            "SOUTH": "YOUR CAR"
        }
    },
    "YOUR CAR": {
        "NAME": "OUTSIDE YOUR CAR",
        "DESCRIPTION": "The door is open, missing its window, the engine is missing, which probably means everything "
                       "inside is stolen.",
        "PATHS": {
            "INSIDE": "INSIDE OF CAR",
            "NORTH": "YOUR HOUSE",
            "EAST": "JOE'S BURGERS"
        }
    },
    "YOUR CAR": {
        "NAME": "INSIDE OF CAR",
        "DESCRIPTION": "Nothing much, just window shards, and a pen on what looks like to be your bloody car mat.",
        "PATHS": {
            "OUTSIDE": "YOUR CAR"
        }
    },
    "YOUR CAR": {
        "NAME": "OUTSIDE OF CAR",
        "DESCRIPTION": "The door is open, missing its window, the engine is missing, which probably means everything "
                       "inside is stolen.",
        "PATHS": {
            "NORTH": "YOUR HOUSE",
            "EAST": "JOE'S BURGERS"
        }
    },
    "JOE'S BURGERS": {
        "NAME": "OUTSIDE JOE'S BURGERS",
        "DESCRIPTION": "One of the best fast food place, Joe's Burgers with extra calories and fat.",
        "PATHS": {
            "WEST": "OUTSIDE OF CAR",
            ""

        }
    },
}


current_node = Hazardine_City["YOUR HOUSE"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'OUTSIDE', 'INSIDE']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_ ')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_code = current_node['PATHS'][command]
            current_node = Hazardine_City[name_of_code]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()