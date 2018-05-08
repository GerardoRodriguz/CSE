class Item(object):
    def __init__(self, name, description, use):
        self.name = name
        self.description = description
        self.use = use

class Weapon(Item):
    def