import pytest


def convert_number_to_reversed_array(n):
    return [int(char) for char in str(n)[::-1]]


@pytest.mark.parametrize("number, expected", [
    (0, [0]),
    (35231, [1, 3, 2, 5, 3])
])
def test_convert_number_to_reversed_array(number, expected):
    assert convert_number_to_reversed_array(number) == expected
