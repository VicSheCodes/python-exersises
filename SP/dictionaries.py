import pytest

my_dict = {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def test_create_dict():
    dict_of_sqr = {i: i ** 2 for i in range(2, 11)}
    print("\n", dict_of_sqr)


def test_my_dict():
    print(f"\n my_dict: {my_dict}")
    print(f"\n my_dict.get(2): {my_dict.get(2)}")
    print(f"\n my_dict.get(10): {my_dict.get(10)}")
    print(f"\n my_dict.keys(): {my_dict.keys()}")
    print(f"\n my_dict.values(): {my_dict.values()}")
    print(f"\n my_dict.items(): {my_dict.items()}")
    print(f"\n my_dict.pop(2): {my_dict.pop(2)}")
    print(f"\n my_dict.pop(10): {my_dict.pop(10)}")
    print(f"\n my_dict.popitem(): {my_dict.popitem()}")
    my_dict.setdefault(11, 121)
    print(f"\n my_dict.setdefault(11, 121): {my_dict.setdefault(11, 121)}")
    print(f"\n my_dict.get(12,0): {my_dict.get(12, 0), 144}")
    print(f"\n my_dict.get(12): {my_dict.get(12)}")


list_of_strings = ['hello', 'world', 'hi', 'ehlol', 'llohe', 'hi', 'owlrd', 'blah', 'aaalllbbb', 'bbblllaaa', 'bbkllla',
                   'labh', 'hlab', 'labh', 'labh', 'labh', 'labh', 'lab']


def group_strings_by_letters(list_of_strings):
    groups = {}
    for str in list_of_strings:
        key = ''.join(sorted(str))
        groups.setdefault(key, []).append(str)
    return list(groups.values())


def test_group_strings_by_letters():
    print(group_strings_by_letters(list_of_strings))


input_sentence = "This is a test sentence. This sentence is for testing."


def test_word_frequency_counter():
    words = input_sentence.split()
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    for k, v in word_frequency.items():
        print(f"{k} : {v}")


if __name__ == '__main__':
    print(f"\n Running tests for {__file__}...")
    pytest.main([__file__])
