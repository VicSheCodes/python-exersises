# The := operator is officially known as the assignment expression operator.

import pathlib
import sys

numbers = [2, 8, 0, 1, 1, 9, 7, 7]


def without_walrus_ex1():
    num_length = len(numbers)
    num_sum = sum(numbers)

    description = {
        "length": num_length,
        "sum": num_sum,
        "mean": num_sum / num_length,
    }

    print(description)
    return description


def with_walrus_ex2():
    description = {
        "length": (len_num := len(numbers)),
        "sum": (num_sum := sum(numbers)),
        "mean": num_sum / len_num,
    }
    print(description)
    return description


def test_without_walrus_ex1():
    assert without_walrus_ex1(numbers) == {
        "length": 8,
        "sum": 35,
        "mean": 4.375,
    }


numbers = [1, 3, 5, 7, 9]


# Without walrus operator
def without_walrus_ex2():
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    print("Squared numbers:", squared_numbers)
    return squared_numbers


# With walrus operator
def with_walrus_ex2():
    squared_numbers = [(sqrt_num := num ** 2) for num in numbers]
    print("Squared numbers:", squared_numbers)
    return squared_numbers


def test_without_walrus_ex2():
    assert without_walrus_ex2() == [1, 9, 25, 49, 81]


def count_lines_and_words_and_characters(filename):
    for filename in sys.argv[1:]:
        path = pathlib.Path(filename)
        counts = [
            (text := path.read_text()).count("\n"),  # Number of lines
            len(text.split()),  # Number of words
            len(text),  # Number of characters
        ]
        print(*counts, path)



if __name__ == "__main__":
    test_without_walrus_ex1()
