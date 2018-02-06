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
print(current_node["NAME"])
print(current_node["DESCRIPTION"])
current_node = world_map["SOUTHHOUSE"]
print(current_node["NAME"])
print(current_node["DESCRIPTION"])