class Animal:
    def speak(self):
        print("\nDefault animal sound")

class Dog(Animal):
    def speak(self):
        print("\nWoof!")

animal = Animal()
print(Animal.__dict__, animal.__dict__)
animal.speak()

dog = Dog()
print(Dog.__dict__, dog.__dict__)
dog.speak()

animal = dog
animal.speak()

dog = animal
dog.speak()
