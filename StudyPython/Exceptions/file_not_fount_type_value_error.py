def func_1():
    # FileNotFoundError
    with open('nonexistent_file.txt', 'r') as file:
        contents = file.read()


def func_2():
    # ValueError
    int('abc')


def func_3():
    # TypeError
    'abc' + 123


if __name__ == '__main__':
    try:
        func_1()
    except FileNotFoundError as e:
        print(e)
    try:
        func_2()
    except ValueError as e:
        print(e)
    try:
        func_3()
    except TypeError as e:
        print(e)
