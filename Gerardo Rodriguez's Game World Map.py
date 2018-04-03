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
            "WEST": "YOUR_HOUSE",
            "OUTSIDE": "YOUR_HOUSE"
        }
    },
    "JIMS_BEDROOM": {
        "NAME": "JIM'S BEDROOM",
        "DESCRIPTION": "It looks like "
                    "a massacre in here with all the bedsheets covered up in a blood and there seems to be a "
                    "figure standing there just staring at a wall. I would recommend to leave.",
        "PATHS": {
            "NORTH": "JIMS_HOUSE_INSIDE",
            "OUTSIDE": "JIMS_HOUSE_INSIDE"
        }
    },
    "JIMS_BATHROOM": {
        "NAME": "JIM'S BATHROOM",
        "DESCRIPTION": "Jim clearly "
                     "does not clean his bathroom at all. But besides that, everything is gone except the toilet, "
                                                                                                  "sink, and bathroom.",
        "PATHS": {
            "SOUTH": "JIMS_HOUSE_INSIDE",
            "OUTSIDE": "JIMS_HOUSE_INSIDE"
        }
    },
    "CASHIER_BACK_JOES_BURGERS": {
        "NAME": "CASHIER BACK",
        "DESCRIPTION": "Shh... there is a mess full of raw meat, blood, and two weird "
                            "human-like creatures. Why not say human? Mostly since they were all bloody, "
                            "ripped clothes, and the fact they are eating frozen beef, chicken, and raw meat.",
        "PATHS": {
            "NORTH": "JOES_BURGERS_INSIDE",
            "SOUTH": "PARKING_LOT",
            "OUTSIDE": "PARKING_LOT"
        }
    },
    "KATES_HOUSE_OUTSIDE": {
        "NAME": "OUTSIDE KATE'S HOUSE",
        "DESCRIPTION": "Kate, Kate, Kate, she was ex before al this and with all this happening, I wonder where "
                      "she is. To shorten the history between you and your ex, you guys only separated because of "
                            "the universities. You haven't had the guts to pass by her house at all...",
        "PATHS": {
            "NORTH": "YOUR_CAR",
            "EAST": "PARKING_LOT",
            "INSIDE": "KATES_HOUSE_INSIDE"
        }
    },
    "KATES_HOUSE_INSIDE": {
        "NAME": "INSIDE KATE'S HOUSE",
        "DESCRIPTION": "Well, considering the whole apocalypse, her house "
                     "is looking decent and mostly everything is in place. There seems to be some stairs leading "
                     "down South, East is a door exit, and West is Kate's kitchen. I keep getting a strange "
                                                                   "feeling someone is in this house...",
        "PATHS": {
            "NORTH": "KATES_HOUSE_OUTSIDE",
            "SOUTH": "KATES_BASEMENT",
            "EAST": "PARKING_LOT",
            "WEST": "KATES_KITCHEN",
            "OUTSIDE": "KATES_HOUSE_OUTSIDE"
        }
    },
    "KATES_KITCHEN": {
        "NAME": "KATE'S KITCHEN",
        "DESCRIPTION": "Nevermind, looks like the house isn't alone after all if you consider a creature eating "
                       "raw meat from "
                "a fridge. Slowly move out of this room. You know, if you want to live.",
        "PATHS": {
            "EAST": "KATES_HOUSE_INSIDE",
            "OUTSIDE": "KATES_HOUSE_INSIDE"
        }
    },
    "KATES_BASEMENT": {
        "NAME": "KATE'S BASEMENT",
        "DESCRIPTION": "You see very little but you can see visible a creature, this is creepy.",
        "PATHS": {
            "NORTH": "KATES_HOUSE_INSIDE",
            "OUTSIDE": "KATES_HOUSE_INSIDE"
        }
    },
    "PARKING_LOT": {
        "NAME": "PARKING LOT",
        "DESCRIPTION": "Just any normal parking lot, empty and blood and guts on the floor.",
        "PATHS": {
            "NORTH": "CASHIER_BACK_JOES_BURGERS",
            "EAST": "MALL_OUTSIDE",
            "WEST": "KATES_HOUSE_OUTSIDE"
        }
    },
    "GAS_STOP_OUTSIDE": {
        "NAME": "OUTSIDE GAS STOP",
        "DESCRIPTION": "If you had a vehicle with low gas, this would be the perfect place to go to but for a snack, not "
                                "so much if you consider blood dripping from the main entrance.",
        "PATHS": {
            "SOUTH": "MALL_OUTSIDE",
            "WEST": "JIMS_HOUSE_OUTSIDE",
            "INSIDE": "GAS_STOP_INSIDE"
        }
    },
    "GAS_STOP_INSIDE": {
        "NAME": "INSIDE GAS STOP",
        "DESCRIPTION": "The aisles are all empty and there is a weird grunting sound coming from the left aisle. Maybe "
                                                                    "turn South to the exit to a store, I think.",
        "PATHS": {
            "SOUTH": "MALL_OUTSIDE",
            "WEST": "GAS_STOP_OUTSIDE",
            "OUTSIDE": "GAS_STOP_OUTSIDE"
        }
    },
    "MALL_OUTSIDE": {
        "NAME": "OUTSIDE MALL",
        "DESCRIPTION": "Oh "
               "crude, this is a mall. Probably the worst place to go to in a zombie apocalypse and has been proven "
               "in many theories. You should be very quiet if you enter you know, if you want...we don't have to "
                                                                                                           "go right?",
        "PATHS": {
            "NORTH": "GAS_STOP_OUTSIDE",
            "WEST": "PARKING_LOT",
            "INSIDE": "MALL_INSIDE"
        }
    },
    "MALL_INSIDE": {
        "NAME": "INSIDE MALL",
        "DESCRIPTION": "Ok, be carefull where you step and how you step, don't attract to much attention "
              "to yourself. North is the shoes store, South seems to be locked and unavailable, and East is the "
                              "breeding ground of these creatures, the food court.",
        "PATHS": {
            "NORTH": "MALLS_SHOE_STORE",
            "EAST": "MALLS_FOOD_COURT",
            "WEST": "MALL_OUTSIDE",
            "OUTSIDE": "MALL_OUTSIDE"
        }
    },
    "MALLS_SHOE_STORE": {
        "NAME": "MALL'S SHOE STORE",
        "DESCRIPTION": "Even though "
                   "those Jordans look really fresh, maybe stick to your shoes because those your wearing look way "
                                            "less bulkier than those fresh Jordans. Just saying.",
        "PATHS": {
            "SOUTH": "MALL_INSIDE",
            "OUTSIDE": "MALL_INSIDE"
        }
    },
    "MALL_FOOD_COURT": {
        "NAME": "MALL FOOD COURT",
        "DESCRIPTION": "Eyes are looking "
                                                "right at you, like dozens. Leave now because I really enjoy life.",
        "PATHS": {
            "WEST": "MALL_INSIDE",
            "OUTSIDE": "MALL_INSIDE"
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