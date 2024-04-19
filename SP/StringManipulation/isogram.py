'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''
import pytest


def is_isogram(string):
    sorted_string = ''.join(sorted(string.lower()))
    sorted_unique_string = ''.join(sorted(set(string.lower())))
    return sorted_string == sorted_unique_string


def is_isogram_2(string):
    return ''.join(sorted(string.lower())) == ''.join(sorted(set(string.lower())))


def is_isogram_3(string):
    sorted_string = ''.join(sorted(string.lower()))
    for i in range(len(string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    return True


def is_isogram_4(string):
    return len(set(string.lower())) == len(string)


@pytest.mark.parametrize("word, expected",
                         [('Dermatoglyphics', True), ('moose', False), ('abnba', False), ('a', True), ("", True)])
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
    assert is_isogram_2(word) == expected
    assert is_isogram_3(word) == expected
    assert is_isogram_4(word) == expected


if __name__ == "__main__":
    print(is_isogram_2('abnba'))
