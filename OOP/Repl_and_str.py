import datetime


class Dog:
    # class attribute
    species = 'Canis familiaris'

    # dunder method instance initializer
    def __init__(self, name='Spike', age=1):
        # instance attributes
        self.name = name
        self.age = age

    # instance method
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    #  provides the official string representation of an object, aimed at the programmer
    @property
    def __repr__(self):
        class_name = type(self).__name__
        return f' {class_name=!r}, class attribute {self.species=!r}, instance attributes are {self.name=!r} {self.age=!r}'

    def today(self):
        return datetime.datetime.now()

    def speak(self, sound='woof'):
        return f"{self.name} says {sound}!"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # def __repr__(self):
    #     class_name = type(self).__name__
    #     return f"{class_name}(title={self.title!r}, author={self.author!r})"
    #
    # def __str__(self):
    #     return f'"{self.title}" by {self.author}'


if __name__ == '__main__':
    dog = Dog()
    print(f" print(Dog)     {dog}")
    print(f" __repr__(Dog) {dog.__repr__}")
    print(f" __str__(Dog)   {dog.__str__()}")

    print(repr(dog.today()))
    print(dog.today().__repr__())
    print(dog.today().__str__())
    print(f"\n{dog.today()}")
    print(f"\n{dog.today()=!r}")
    print(f"{dog.today()=!s}")
    print(f"{dog.today()=}\n")

    # odyssey = Book("The Odyssey", "Homer")
    # print(repr(odyssey))
    # print(str(odyssey))

    miles = JackRussellTerrier("Miles", 4)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 5)

    print(f"{miles.species=}")
    print(f"{buddy.name=}")
    print(jack)
    print(f"{jack= !s}")
    print(f"{jim.speak('Woof')=}")
    print(f"{miles.speak()=}")
