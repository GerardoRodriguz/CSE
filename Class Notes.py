# Defining a class
class Cat(object):
    # TWO underscores before and after
    def _init_(self, color, pattern):
        # Things that a Cat has
        self.color = color
        self.pattern = pattern

    # Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "happy"
        print("You play with the cat")


# Instantiating (creating) two cats
cute_cat = Cat("brown", "spots")
cute_cat2 = Cat("grey", "no spots")

# Getting information about the cats
print(cute_cat.color)
print(cute_cat2.state)
print(cute_cat2.color)

cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)


class Car(object):
    def __init__(self, color, brand, num_of_cylinders):
        self.color = color
        self.brand = brand
        self.cylinders = num_of_cylinders
        self.engineOn = False

    def turn_on(self):
        if self.engineOn:
            print("Nothing Happens")
        else:
            print("The engine turns on")
            self.engineOn = True
    def move_foward(self):
        if self.engineOn:
            print("You move foward")
        else:
            print("Nothing Happens")
    def turnOff(self):
        if self.engineOn:
            self.engineOn = False
            print("The engine turns off")
        else:
            print("Nothing Happens")

my_car = Car(4, "Subaru", "Blue")

my_car.turn_on()
my_car.move_foward()
my_car.turnOff()

