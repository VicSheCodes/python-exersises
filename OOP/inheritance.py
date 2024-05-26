class Parent:
    homeland = "England"
    role = "Parent"

    def __init__(self, name="X"):
        self.name = name


class Child(Parent):
    role = "Child"

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, role={self.role!r})"


if __name__ == '__main__':
    Rob=Parent("Robert")
    Sally=Child("Sally")
    Prince = Rob

    print(f"{Rob.name= !r}")
    print(f"{Rob.role= !r}")
    print(f"{Rob.__class__= !r}")
    print(f"{Rob.__class__.__name__= !r}")
    print(f"{Rob.__repr__()= !r}")
    print(Sally.name)
    print(Sally.role)
    print(Sally.__class__)
    print(Sally.__class__.__name__)
    print(Sally.__repr__())
    print(f"{Sally.homeland= !r}")

    print(f"{Prince.name=!r} {Prince.role=!r} {Prince.__class__=!r} {Prince.__repr__()=!r}")

