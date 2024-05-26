class Animal:
    def __init__(self, species):
        self.species = species
        print("Animal constructor called")

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")  # Calling the constructor of the superclass
        self.name = name
        print("Dog constructor called")

# Creating an instance of Dog
dog = Dog("Buddy")
