"""
Filtering Prime Numbers:
Generate prime numbers up to 20:
(num for num in range(2, 21) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))).
Combining and Filtering Zip:
Generate pairs of even numbers from two lists:
((x, y) for x, y in zip(list1, list2) if x % 2 == 0 and y % 2 == 0).
Extracting Unique Elements:
Generate unique elements from a list:
(x for x in my_list if my_list.count(x) == 1).
Parsing CSV Data:
Generate tuples from CSV rows, skipping header:
(tuple(row) for row in csv_data if not row.startswith('header')).
Selecting Odd Length Strings:
Generate strings with odd length:
(string for string in string_list if len(string) % 2 != 0).
"""
import pytest


def perform_oper(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b if b != 0 else None


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, [5, -1, 6, 0.6666666666666666]),
    (10, 2, [12, 8, 20, 5]),
    (0, 5, [5, -5, 0, 0.0])
])
def test_perform_oper(a, b, expected):
    result = list(perform_oper(a, b))
    assert result == expected


def sum_numbers(*args):
    return sum(args)


def test_sum_numbers():
    assert sum_numbers(1, 2, 3) == 6
    assert sum_numbers(1, 2, 3, 4) == 10
    assert sum_numbers(1, 2, 3, 4, 5) == 15
    assert sum_numbers(1, 2, 3, 4, 5, 6) == 21


matrix_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
def transpose_matrix(*matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def test_transpose_matrix():
    print(transpose_matrix(*matrix_list))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose_matrix(*matrix_list) == [[1, 4, 7], [2, 5,8], [3, 6, 9]]


"""
When pytest.main([__file__]) is called, pytest will search the specified file for test functions
 (functions whose names start with test_) and run them. In this case, __file__ represents the current 
 Python script file, so pytest will run tests defined within that file.
 This allows you to conveniently run tests from within your script,"""

if __name__ == '__main__':
    #  pytest.main([__file__])
    print(*(result for result in perform_oper(20, 2)))
    print(list(number for number in iter(perform_oper(20, 2))))
    # print(total)
