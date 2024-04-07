from copy import copy, deepcopy
import itertools


def list_examples():
    my_list = [1, 2, 3, 4, 5, 3, 5, 6, 7, 8, 9, 10]
    print("\nmy_list ", my_list)
    my_list.append(11)
    print("my_list.append(11) ", my_list)
    my_list.remove(11)
    print("my_list.remove(11) ", my_list)
    my_list.pop()
    print("my_list.pop()  ", my_list)
    my_list.pop(3)
    print("my_list.pop(3)", my_list)
    my_list.insert(0, 11)
    print("my_list.insert(0,11)", my_list)
    del my_list[3]
    print("del my_list[3]", my_list)
    my_list.append(3)
    print("my_list.append[3]", my_list)
    my_list.reverse()
    print("my_list_reverse()", my_list)
    my_list.sort()
    print("my_list.sort()", my_list)
    my_list.sort(reverse=True)
    print("my_list.sort(reverse=True)", my_list)
    print("my_list.count(3)", my_list.count(3))
    print("my_list.index(2)", my_list.index(2))
    second_list = my_list.copy()
    print("second_list = my_list.copy()", second_list)
    my_list.clear()
    print("my_list.clear()", my_list)


def examples():
    # Performing mathematical operations on the entire list
    my_list = [2, 3, 5, 7, 11]
    squared_list = [x ** 2 for x in my_list]  # list comprehension
    # output => [4 , 9 , 25 , 49 , 121]
    squared_dict = {x: x ** 2 for x in my_list}  # dict comprehension
    # output => {11: 121, 2: 4 , 3: 9 , 5: 25 , 7: 49}

    # Performing conditional filtering operations on the entire list
    my_list = [2, 3, 5, 7, 11]
    squared_list = [x ** 2 for x in my_list if x % 2 != 0]  # list comprehension
    # output => [9 , 25 , 49 , 121]
    squared_dict = {x: x ** 2 for x in my_list if x % 2 != 0}  # dict comprehension
    # output => {11: 121, 3: 9 , 5: 25 , 7: 49}


def combine_multiple_lists_into_one():
    # Combining multiple lists into
    # Comprehensions allow for multiple iterators and hence, can be used to combine multiple lists into one.

    a = [1, 2, 3]
    b = [7, 8, 9]
    [(x + y) for (x, y) in zip(a, b)]  # parallel iterators
    # output => [8, 10, 12]
    [(x, y) for x in a for y in b]  # nested iterators
    # output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]


# A similar approach of nested iterators (as above) can be applied to flatten a multidimensional
# list or work upon its inner elements.
def flattening_a_multi_dimensional_list():
    my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    c = [x for temp in my_list for x in temp]
    print(f"\n Original list:     {my_list}")
    print(f"\n Flattened list:     {c}")
    # output => [10, 20, 30, 40, 50, 60, 70, 80, 90]


# Note: List comprehensions have the same effect as the map method in other languages.
# They follow the mathematical set builder notation rather than map and filter functions in Python.


# 6. What is lambda in Python? Why is it used?
# Lambda is an anonymous function in Python, that can accept any number of arguments,
# but can only have a single expression. It is generally used in situations requiring an anonymous
# function for a short time period. Lambda functions can be used in either of the two ways:

# Assigning lambda functions to a variable:
mul = lambda a, b: a * b
print(mul(2, 5))  # output => 10


# Wrapping lambda functions inside another function:
def myWrapper(n):
    return lambda a: a * n


mulFive = myWrapper(5)
print(mulFive(2))  # output => 10


# Shallow Copy is a bit-wise copy of an object. The copied object created has an exact copy
# of the values in the original object. If either of the values is a reference to other objects,
# just the reference addresses for the same are copied.
# Deep Copy copies all values recursively from source to target object, i.e. it even duplicates
# the objects referenced by the source object.


def demonstrate_deep_and_shallow_copy():
    list_1 = [1, 2, [3, 5], 4]
    print(f"\n Original list_1:     {list_1}")
    ## shallow copy
    list_2 = copy(list_1)
    print(f"\n Shallow copy list_2: {list_2}")
    list_2[3] = 7  # will change only shallow copy
    list_2[2].append(6)  # will change both original and copy as thy reference the same object
    print(
        f"\n Shallow copy list_2 change nested list to '[3, 5, 6]' and  regular element 3 to '7': {list_2}")  # output => [1, 2, [3, 5, 6], 7]
    print(f"\n Original list_1 was also changed in nested list : {list_1}")  # output => [1, 2, [3, 5, 6], 4]
    ## deep copy
    list_3 = deepcopy(list_1)
    print(f"\n Deep copy list_3: {list_3}")
    list_3[3] = 8
    list_3[2].append(7)
    print(
        f"\n Deep copy list_3 after changes to nested list and regular element: {list_3}")  # output => [1, 2, [3, 5, 6, 7], 8]
    print(f"\n Original list_1 wasn't changed: {list_3}")  # output => [1, 2, [3, 5, 6], 4]


def demonstrate_deep_and_shallow_copy_2():
    print(f"\n demonstrate_deep_and_shallow_copy_2 \n")
    original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    shallow_copy = copy(original_list)
    shallow_copy_2 = original_list.copy()
    print(f"\n Shallow copy_: {shallow_copy}")
    print(f"\n Shallow copy_2: {shallow_copy_2}")
    print(f"\n Is shallow_copy an original_list? {shallow_copy is original_list}")  # False
    print(
        f"\n Is shallow_copy referenced objects - nested lists are the one from the original_list? {shallow_copy[0] is original_list[0]}")  # True

    deep_copy = deepcopy(original_list)  # deep copy
    print(f"\n Deep copy: {deep_copy}")
    print(f"\n Is deep_copy an original_list? {deep_copy is original_list}")  # True
    deep_copy[0][0] = 100
    print(
        f"\n Is deep_copy referenced objects - nested lists are the one from the original {original_list[0][0] is deep_copy[0][0]}")  # True
    print(f" deep_copy     {deep_copy}")  # [[100, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f" original_list {original_list}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def flattening_a_multi_dimensional_list_comprehension():
        nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        flattened_list = [item for sublist in nested_list for item in sublist]
        print(f"\n flattened list: {flattened_list}")
        for sublist in nested_list:
            print(*sublist)
        for sublist in nested_list:
            print(*sublist, end=' ')


def test_flattening_using_itertools():
    list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_2 = [1, 2, 3, 4, 5, 6]
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = list(itertools.chain(list_1, list_2))
    print(f"\n flattened list: {flattened_list}")
    flattened_list = list(itertools.chain(*nested_list))
    print(f"\n flattened list: {flattened_list}")


if __name__ == "__main__":
    demonstrate_deep_and_shallow_copy()
    flattening_a_multi_dimensional_list()
    demonstrate_deep_and_shallow_copy_2()
