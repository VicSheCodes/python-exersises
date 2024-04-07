"""
 In Python, the * operator can be used for unpacking elements from an iterable,
 such as a list, tuple, or set, into individual elements. This is particularly useful
 when you have a collection of values, and you want to pass them as arguments to a function,
or assign them to variables.

"""

my_list = [1, 2, 3, 4, 5]


def slicing_using_unpacking():
    first, *middle, last = my_list  # This assigns 1 to first, [2, 3, 4] to middle, and 5 to last
    print(first, middle, last)


def printing_variables(*argv):
    print(argv)


if __name__ == '__main__':
    printing_variables(*my_list)
