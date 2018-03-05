world_map = {
    "WEST HOUSE": {
        "NAME": "WEST OF HOUSE",
        "DESCRIPTION": "You are west of a small house",
        "PATHS": {
            "NORTH": "NORTHHOUSE",
            "SOUTH": "SOUTHHOUSE"
        }
    },
    "NORTHHOUSE": {
        "NAME": "NORTH OF HOUSE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "WESTHOUSE"
        }
    },
    "SOUTHHOUSE": {
        "NAME": "SOUTH OF HOUSE",
        "DESCRIPTION": "Insert description here",
        "PATHS": {
            "WEST": "WESTHOUSE"
        }
    }
}

current_node = world_map["WEST HOUSE"]
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input('>_ ')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_code = current_node['PATHS'][command]
            current_node = world_map[name_of_code]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not found.")
    print()


