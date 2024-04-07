"""
Iterable object (e.g., a list, tuple, string, etc.) from which you want to create an iterator.
When you call iter() on an iterable object, it returns an iterator object that allows you to traverse the elements
of the iterable one by one using the next() function or in a loop.
"""
from collections import namedtuple


def tuple_ex():
    '''
    The field names are defined as a list of strings.
    The namedtuple constructor is used to create a new namedtuple type named days_of_week with the specified field names
    An instance of the days_of_week namedtuple is created by passing values corresponding to each field.
    '''

    # Define field names as a sequence of strings
    field_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Create a namedtuple type with field names
    days_of_week_namedtuple = namedtuple('days_of_week', field_names)

    # Create an instance of the days_of_week namedtuple
    days = days_of_week_namedtuple("1", "2", "3", "4", "5", "6", "7")

    # Access elements by field names
    print(days.Monday)  # Output: 2


if __name__ == '__main__':
    iterable_object_list = [1, 2, 1, 3, 4, 4, 5, 9, 6, 6]
    iterable_object_dict = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55, 'f': 66}
    iterable_object_set = {'a', 'b', 'c', 'd', 'e', 'f'}
    iterable_object_tuple = ("Sunday", "Mondday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    days_of_week = namedtuple('days_of_week', ["Sunday", "Mondday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    iterable_object_namedtuple = days_of_week("1", "2", "3", "4", "5", "6", "7")
    iterable_object_string = 'Hello World!'

    iterable_from_list = iter(iterable_object_list)
    iterable_from_dict = iter(iterable_object_dict)
    iterable_from_set = iter(iterable_object_set)
    iterable_from_tuple = iter(iterable_object_tuple)
    iterable_from_string = iter(iterable_object_string)
    iterable_from_days_of_week = iter(iterable_object_namedtuple)

    # Iterate over objects
    while True:
        try:
            print(next(iterable_from_list))
        except StopIteration:
            break

        try:
            print(next(iterable_from_dict))
        except StopIteration:
            break

        try:
            print(next(iterable_from_set))
        except StopIteration:
            break

        try:
            print(next(iterable_from_tuple))
        except StopIteration:
            break

        try:
            print(next(iterable_from_string))
        except StopIteration:
            break
