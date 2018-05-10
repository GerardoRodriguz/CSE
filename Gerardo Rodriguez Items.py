class Item(object):
    def __init__(self, name, description, use, heal):
        self.name = name
        self.description = description
        self.use = use
        self.heal = heal


class Healing(Item):
    def __init__(self, name, description, use, heal):
        super(Healing, self).__init__(name, description, use)
        self.name = name
        self.description = description
        self.use = use
        self.heal = heal

        def heal(self):
            if Burger or Soda or Enchancer in inventory:
                self.heal += Character.health


class Burger(Healing):
    def __init__(self, name, description, use, heal):
        super(Burger, self).__init__(name, description, use, heal)

        def heal(self):
            if Burger in inventory:
                print("I would suggest to eat this delicious burger even though I doubt you have an appetite.")
                self.heal += Character.health


class Soda(Healing):
    def __init__(self, name, description, use, heal ):
        super(Soda, self).__init__(name, description, use, heal)

        def heal(self):
            if Soda in inventory:
                print("Nothing better than a nice soda.")
                self.heal += Character.health


class Amour(Item):
    def __init__(self, name, description, use, durability):
        super(Amour, self).__init__(name, description, use, durability)
        self.name = name
        self.description = description
        self.use = use
        self.durability = durability

        def Protection(self):
            if Amour in inventory:
                self.durability += Character.health