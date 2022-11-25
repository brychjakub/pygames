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

#create two dog objects
dog_1 = Dog("spot", "male", 3)
dog_2 = Dog("caty", "female", 12)

#access atributes of objects
print(dog_1.age)
print(dog_2.gender)
print()

dog_1.eat()
dog_2.eat()
print()

dog_2.bark(False)
dog_1.bark(True)

dog_1.compute_age()
dog_2.compute_age()