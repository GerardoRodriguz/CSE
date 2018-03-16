Hazardine_City = {
    "YOUR_HOUSE": {
        "NAME": "YOUR HOUSE",
        "DESCRIPTION": "Welcome, the day has come, the undead rule the world but, you can make a difference by "
                       "finding a cure. East is where your neighbors live, and South is your car, broken because of "
                       "all the anarchy.",
        "PATHS": {
            "EAST": "NEIGHBORS",
            "SOUTH": "YOUR CAR"
        }
    },
    "CAR_OUTSIDE": {
        "NAME": "OUTSIDE YOUR CAR",
        "DESCRIPTION": "The door is open, missing its window, the engine is missing, which probably means everything "
                       "inside is stolen.",
        "PATHS": {
            "INSIDE": "INSIDE OF CAR",
            "NORTH": "YOUR HOUSE",
            "EAST": "JOE'S BURGERS"
        }
    },
    "CAR_INSIDE": {
        "NAME": "INSIDE OF CAR",
        "DESCRIPTION": "Nothing much, just window shards, and a pen on what looks like to be your bloody car mat.",
        "PATHS": {
            "OUTSIDE": "YOUR CAR"
        }
    },
    "JOES_BURGERS_OUTSIDE": {
        "NAME": "OUTSIDE JOE'S BURGERS",
        "DESCRIPTION": "One of the best fast food place, Joe's Burgers with extra calories and fat.",
        "PATHS": {
            "WEST": "OUTSIDE OF CAR",
            "NORTH": "JIMS_HOUSE_OUTSIDE",
            "SOUTH": "PARKING_LOT",
            "INSIDE": "JOES_BURGERS_INSIDE"

        }
    },
    "JIMS_HOUSE_OUTSIDE": {
        "NAME": "OUTSIDE JIM'S HOUSE",
        "DESCRIPTION": "This is your neighbor's house, he was a quiet neighbor and to "
                          "say the truth, he was creepy. His house looks all messed up because of anarchy and the "
                                "door is wide open. Strange...",
        "PATHS": {
            "SOUTH": "JOES_BURGERS_OUTSIDE",
            "EAST": "YOUR_HOUSE",
            "WEST": "GAS_STOP_OUTSIDE",
            "INSIDE": "JIMS_HOUSE_INSIDE",

        }
    },
    "JIMS_HOUSE_INSIDE": {
        "NAME": "INSIDE JIM'S HOUSE",
        "DESCRIPTION": "Looks like someone already looted the place, only a table with a missing leg "
                         "remains with the furniture. North is Jim's bathroom, South is Jim's bedroom, East is an "
                                       "exit, and another exit behind you.",
        "PATHS": {
            "NORTH": "JIMS_BATHROOM",
            "SOUTH": "JIMS_BEDROOM",
            "EAST": "GAS_STOP_OUTSIDE",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "JIMS_BEDROOM": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "JIMS_BATHROOM": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "CASHIER_BACK_JOES_BURGERS": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "KATES_HOUSE_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "KATES_HOUSE_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "KATES_KITCHEN": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "KATES_BASEMENT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "PARKING_LOT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "GAS_STOP_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "GAS_STOP_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "MALL_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "MALL_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "MALLS_SHOE_STORE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
    "MALL_FOOD_COURT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            "NORTH": "",
            "SOUTH": "",
            "EAST": "",
            "WEST": "",
            "INSIDE": "",
            "OUTSIDE": ""
        }
    },
}

# Game controller
current_node = Hazardine_City["YOUR HOUSE"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'OUTSIDE', 'INSIDE']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_ ')
    if command == "quit":
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