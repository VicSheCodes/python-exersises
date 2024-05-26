class MyStaticMethod():

    @staticmethod
    def add(x, y):
        return x+y


print(MyStaticMethod().add(a:=100, 1))
print(MyStaticMethod.add(a, 200))
