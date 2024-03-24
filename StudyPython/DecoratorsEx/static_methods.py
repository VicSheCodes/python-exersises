class MathUtils():
    def __init__(self, a = 10, b = 20):
        self.a = a
        self.b = b
        pass

    def add(self):
        return self.a + self.b

    @staticmethod
    def add2(a, b):
        return a + b


if __name__ == '__main__':

    math_utils_1 = MathUtils(2,8)
    math_utils_2 = MathUtils()
    print(math_utils_1.add())
    print(math_utils_2.add())

    print(MathUtils.add2(2, 3))
