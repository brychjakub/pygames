class Dog():
    """a class to represent a general dog"""


    def __init__(self, my_name, my_gender, my_age):
        self.name = my_name
        self.gender = my_gender
        self.age = my_age


    def eat(self):
        if self.gender == "male":
            print("here " + self.name + "! good boy!")
        else:
            print("here, girl " + self.name)


    def bark(self, is_loud):
        if is_loud:
            print("WOOF WOOF")
        else:
            print("woofi...")

    def compute_age(self):
        dog_years = self.age*7
        print(self.name + "is " + str(dog_years) + " years old")


class Beagle(Dog):
    #a class to represent a specific type of dog

    def __init__(self, my_name, my_gender, my_age, is_gun_shy):
        super().__init__(my_name, my_gender, my_age)
        self.is_gun_shy = is_gun_shy


    def hunt(self):
        if not self.is_gun_shy:
            self.bark(True)
            print(self.name + " just brought back a duck.")
        else:
            print(self.name + " is not a good hunting dog.")

dog1 = Beagle("kady", "female", 10, False)
dog1.eat()
dog1.compute_age()
dog1.hunt()