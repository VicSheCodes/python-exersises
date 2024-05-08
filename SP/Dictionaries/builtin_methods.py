"""
Sure, here are the built-in methods of the Python dictionary object:

1. `clear()`: Removes all items from the dictionary.
2. `copy()`: Returns a shallow copy of the dictionary.
3. `fromkeys(iterable[, value])`: Returns a new dictionary with keys from the iterable and values set to the
 specified value (default is `None`).
4. `get(key[, default])`: Returns the value for the specified key. If the key is not found, it returns the
 default value (default is `None`).
5. `items()`: Returns a view object that displays a list of a dictionary's key-value pairs as tuples.
6. `keys()`: Returns a view object that displays a list of all the keys in the dictionary.
7. `pop(key[, default])`: Removes the item with the specified key and returns its value. If the key is not found,
 it returns the default value (default is `None`).
8. `popitem()`: Removes and returns the last inserted key-value pair as a tuple.
9. `setdefault(key[, default])`: Returns the value of the specified key. If the key does not exist,
 inserts the key with the specified value (default is `None`) and returns the value.
10. `update(iterable)`: Updates the dictionary with the key-value pairs from the specified iterable.
11. `values()`: Returns a view object that displays a list of all the values in the dictionary.


"""


def test_using_get():
    # Example using get()
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    value = dictionary.get('b')
    print()
    print(value)  # Output: 2

    # Specifying default value
    value = dictionary.get('d', 'Key not found')
    print(value)  # Output: 'Key not found'
    value = dictionary.get('d', len(dictionary))
    print(value)  # Output: '3
    dictionary['d'] = dictionary.get('d', len(dictionary))


def test_create_dictionary_with_appearance_count():
    word = 'Mississippi'
    word_count = {word: len(word)}
    print(word_count)  # Output: {'Mississippi': 11}

    rivers = ['Mississippi', 'Nile', 'Amazon', 'Yangtze', 'Danube', 'Ganges']
    river_count = {(name, len(name)): name.count('i') for name in rivers}
    print(f"\n {river_count}")


def test_using_fromkeys():
    # Example using fromkeys()
    keys = ['a', 'b', 'c']
    value = 0  # Default value
    dictionary = dict.fromkeys(keys, value)
    print(dictionary)  # Output: {'a': 0, 'b': 0, 'c': 0}
    rivers = ['Mississippi', 'Nile', 'Amazon', 'Yangtze', 'Danube', 'Ganges']

    rivers_dict = dict.fromkeys(rivers, 0)
    print(f"\n {rivers_dict}")
    rivers_dict = {river_name: len(river_name) for river_name in rivers}
    print(f"\n {rivers_dict}")


def test_using_pop():
    # Example using pop()
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    value = dictionary.pop('b')
    print(value)  # Output: 2
    print(dictionary)  # Output: {'a': 1, 'c': 3}

    # Specifying default value
    value = dictionary.pop('d', 'Key not found')
    print(value)  # Output: 'Key not found'
