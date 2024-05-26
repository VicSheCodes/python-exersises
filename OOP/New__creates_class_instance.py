class MyClass():
    def __new__(cls, *args, **kwargs):
        print("\n Creating an instance of the class. ")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name="MyClass"):
        print("\n Initializing an instance of the class. ")
        self.name = name

a = MyClass()
print(a.__dict__)