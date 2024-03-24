"""
built-in functions in Python include:

ma(): used to map a function over an iterable.
filter(): Used to filter elements from an iterable based on a specified function.
reduce(): Used to apply a function to the items of an iterable cumulatively.
sorted(): Used to sort elements of an iterable.
zip(): Used to combine multiple iterables into a single iterator of tuples.
enumerate(): Used to add a counter to an iterable and return it as an enumerate object.
max(), min(): Used to find the maximum or minimum element in an iterable.
any(), all(): Used to check if any or all elements of an iterable are true.

"""


from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


def test_demo_filter():
    even_numbers = filter(is_even, lst)
    eee = list(even_numbers)
    yyy = list(even_numbers)
    print("\n output: ", list(filter(is_even, lst)))
    print("\n output: ", list(even_numbers))  # This will be an empty list
    # print("\n output: ", list(eee))
    # print("\n output: ", list(yyy))


# Define a function to concatenate two strings
def concatenate_strings(x, y):
    return x + " " + y


def sum_numbers(x, y):
    return x + y


def test_maximum_sec():
    numbers1 = [5, 9, 3, 7, 2, 11]
    numbers2 = [(5, 9, 3), (9, 3, 7), (3, 7, 2), (7, 2, 11)]  # List of tuples
    sum1 = reduce(sum_numbers, numbers1)
    print("sum value:", sum1)


def make_negative(x):
    return -x


def test_make_negative():
    numbers = [5, 9, 3, 7, 2, 11]
    converted_to_negative = list(map(make_negative, numbers))
    print(f" \n Converted list is: {converted_to_negative}")


def test_concatenate_strings():
    strings = ["Hello", "world,", "how", "are", "you?"]

    # Use reduce to concatenate the strings
    concatenated_string = reduce(concatenate_strings, strings)

    print("Concatenated string:", concatenated_string)


def test_sorting():
    # Sort a list of numbers using sorted()
    numbers = [5, 2, 7, 1, 9]
    sorted_numbers = sorted(numbers, reverse=True)

    print(sorted_numbers)  # Output: [1, 2, 5, 7, 9]


def test_zip():
    # Combine two lists into tuples using zip()
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    combined = zip(names, ages)

    print(list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


def test_enumerate():
    # Enumerate a list of names
    names = ['Alice', 'Bob', 'Charlie']
    enumerated_names = enumerate(names)

    print(list(enumerated_names))  # Output: [(0, 'Alice'), (1, 'Bob'), (2, 'Charlie')]


def test_max_min():
    # Find the maximum and minimum elements in a list
    numbers = [5, 2, 7, 1, 9]
    max_number = max(numbers)
    min_number = min(numbers)

    print(max_number, min_number)  # Output: 9 1


def test_any_all():
    # Check if any or all elements of a list are even
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [1, 3, 5, 7, 9]
    are_any_even = any(num % 2 == 0 for num in numbers1)
    are_all_even = all(num % 2 == 0 for num in numbers2)

    print(are_any_even, are_all_even)  # Output: True False


strings = ["abl", "bla", "lllba", "sddd", "ddsd", "sdsd", "sdsd", "sdsd", "sdsd", "sds", "alb", "aaalllbbb",
           "bbblllaaa", "bbkllla", "sdsd"]


def find_equal_strings():
    result = {}
    for string in strings:
        key = ''.join(sorted(string))
        result.setdefault(key, []).append(string)
    return list(result.values())


def test_find_equal_strings():
    print("\n", find_equal_strings())


def group_strings_by_letters(strings):
    groups = {}
    for string in strings:
        key = ''.join(sorted(string))  # Sort the letters of the string to create a key
        groups.setdefault(key, []).append(string)  # Append the string to the corresponding group
    return list(groups.values())  # Return the values of the dictionary as a list of groups


def test_group_strings_by_letters():
    strings = ['hello', 'world', 'hi', 'ehlol', 'llohe', 'hi', 'owlrd']
    groups = group_strings_by_letters(strings)
    print("\n", groups)


def test_using_append_extends():
    # Using append()
    list1 = [1, 2, 3]
    list1.append([4, 5])
    print(list1)  # Output: [1, 2, 3, [4, 5]]

    # Using extend()
    list2 = [1, 2, 3]
    list2.extend([4, 5])
    print(list2)  # Output: [1, 2, 3, 4, 5]


def test_sort_tuples_to_list():
    tuples = [(5, 9), (7, 2), (3, 7), (2, 2, 2), (11, 5)]
    sorted_numbers = []
    for tup in tuples:
        sorted_numbers.extend(sorted(tup, reverse=False))
    new_list = list(sorted_numbers)

    print(sorted_numbers)
    print(new_list)
