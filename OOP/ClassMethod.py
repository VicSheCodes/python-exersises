class CarPool:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.cars = []
        CarPool.total_cars += 1

    @classmethod
    def display_total_cars(cls):
        return cls.total_cars


print(CarPool.display_total_cars())

# Creating instances of Car
car1 = CarPool("Toyota", "Camry")
car2 = CarPool("Honda", "Civic")

print(CarPool.display_total_cars())




