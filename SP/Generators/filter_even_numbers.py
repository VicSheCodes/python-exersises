
numbers = [1, 2, 3, 4, 5, 6]
only_odd_numbers = [num for num in numbers if num % 2 != 0]


def filter_even_numbers_or_none(list_of_numbers):
    for num in list_of_numbers:
        if num % 2 == 0:
            yield num
    yield None


if __name__ == '__main__':
    print(* (num for num in filter_even_numbers_or_none(numbers) if num is not None))
    print(*filter_even_numbers_or_none(only_odd_numbers))