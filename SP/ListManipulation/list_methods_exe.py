'''
append(): Adds an element to the end of the list.
extend(): Appends elements from another list to the end of the list.
insert(): Inserts an element at the specified position.
remove(): Removes the first occurrence of a specified element from the list.
pop(): Removes the element at the specified position, and returns it.
clear(): Removes all elements from the list.
index(): Returns the index of the first occurrence of a specified value.
count(): Returns the number of elements with the specified value.
sort(): Sorts the list.
reverse(): Reverses the order of the list.
copy(): Returns a copy of the list.
len(): Returns the number of elements in the list.
max(): Returns the maximum value in the list.
min(): Returns the minimum value in the list.
sum(): Returns the sum of all elements in the list.
any(): Returns True if any element in the list is True, otherwise returns False.
all(): Returns True if all elements in the list are True, otherwise returns False.
slice(): Returns a slice of the list based on the specified start, end, and step parameters.
enumerate(): Returns an enumerate object, containing tuples of the index and value for each element in the list.
zip(): Returns an iterator that aggregates elements from two or more lists.
map(): Applies a function to every item in the list.
filter(): Filters elements from the list based on a function.
reversed(): Returns a reverse iterator of the list.

'''
import random


def test_create_list(n=5):
    lst = [list(range(n))]
    print(f"\n lst = [list(range(n))]  result is: {lst}")
    lst_1 = list(range(1, 6))
    print(f"\n lst_1 = list(range(1, 6))  result is: {lst_1}")
    lst_2 = [x for x in range(1, 6)]
    print(f"\n lst_2 = [x for x in range(1, 6)]  result is: {lst_2}")
    random_numbers = [random.randint(1, 100) for _ in range(6)]
    print(f"\n random_numbers = [random.randint for _ in range(6)]  result is: {random_numbers}")


# append() and extend():
# Create a list with nested lists as elements. Use append() and extend() to add new elements
# and see how they differ in handling nested lists.
# range(i): This function generates a sequence of numbers from 0 to i-1. For example,
# range(4) generates the sequence [0, 1, 2, 3] because it starts at 0 and ends at 3 (not including 4).
def append_extend_elements(n=5):
    nested_list = []
    for i in range(1, n+1):
        nested_list.append(list(range(i)))
    print(f" \n nested_list for n={n} {nested_list}")
    return nested_list


def test_append_extend_elements():
    assert append_extend_elements(6) == [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5]]
    assert append_extend_elements(4) == [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
    assert append_extend_elements(1) == [[0]]
    assert append_extend_elements(0) == []

# List Manipulation with Recursion:
# Write a function that takes a list of integers as input and returns a new list
# with each element multiplied by 2 using recursion. Avoid using loops or list comprehension.
