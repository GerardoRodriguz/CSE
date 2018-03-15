Hazardine_City = {
    "YOUR_HOUSE": {
        "NAME": "YOUR HOUSE",
        "DESCRIPTION": "Welcome, the day has come, the undead rule the world but, you can make a difference by "
                       "finding a cure. East is where your neighbors live, and South is your car, broken because of "
                       "all the anarchy.",
        "PATHS": {
            "EAST": "NEIGHBORS",
            "SOUTH": "CAR_OUTSIDE"
        }
    },
    "CAR_OUTSIDE": {
        "NAME": "OUTSIDE YOUR CAR",
        "DESCRIPTION": "The door is open, missing its window, the engine is missing, which probably means everything "
                       "inside is stolen.",
        "PATHS": {
            "INSIDE": "CAR_INSIDE",
            "NORTH": "YOUR_HOUSE",
            "EAST": "JOES_BURGERS_OUTSIDE"
        }
    },
    "CAR_INSIDE": {
        "NAME": "INSIDE OF CAR",
        "DESCRIPTION": "Nothing much, just window shards, and a pen on what looks like to be your bloody car mat.",
        "PATHS": {
            "OUTSIDE": "CAR_OUTSIDE"
        }
    },
    "JOES_BURGERS_OUTSIDE": {
        "NAME": "OUTSIDE JOE'S BURGERS",
        "DESCRIPTION": "One of the best fast food place, Joe's Burgers with extra calories and fat.",
        "PATHS": {
            "WEST": "CAR_OUTSIDE",
            "NORTH": "JIMS_HOUSE_OUTSIDE",
            "SOUTH": "PARKING_LOT",
            "INSIDE": "JOES_BURGERS_INSIDE"
        }
    },
    "PARKING_LOT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "JIMS_HOUSE_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "JIMS_HOUSE_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "JIMS_BEDROOM": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "JIMS_BATHROOM": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "CASHIER_BACK_JOES_BURGERS": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "KATES_HOUSE_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "KATES_HOUSE_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "KATES_KITCHEN": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "KATES_BASEMENT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "GAS_STOP_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "GAS_STOP_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "MALL_OUTSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "MALL_INSIDE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "MALLS_SHOE_STORE": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
        }
    },
    "MALL_FOOD_COURT": {
        "NAME": "",
        "DESCRIPTION": "",
        "PATHS": {
            ""
            ""
            ""
            ""
            ""
            ""
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
    #