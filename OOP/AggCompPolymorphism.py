class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class PetOwner:
    def __init__(self):
        # Aggregation: PetOwner contains a list of Animal objects
        self.animals = []

    def add_animal(self, animal):
        # Aggregation: Adding an Animal object to the list
        self.animals.append(animal)

    def make_all_animals_speak(self):
        for animal in self.animals:
            # Polymorphism: The PetOwner doesn't need to know the specific subclass of Animal
            # It just knows that each Animal has a speak() method
            print(animal.speak())

# Example usage:
owner = PetOwner()

# Composition: PetOwner directly creates instances of Dog and Cat
owner.add_animal(Dog())
owner.add_animal(Cat())

owner.make_all_animals_speak()
