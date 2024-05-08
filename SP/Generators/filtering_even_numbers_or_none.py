
list_of_numbers = [1, 2, 3, 4, 5, 6]


def filtering_even_numbers_or_none(list_of_numbers):
    for num in list_of_numbers:
        if num % 2 == 0:
            yield num


def test_filtering_even_numbers_or_none(list_of_numbers):
    result = filtering_even_numbers_or_none(list_of_numbers)
    for num in result:
        print(num)


def filtering_even_numbers_or_none_1():
    yield (x for x in list_of_numbers if x % 2 == 0)


def filtering_even_numbers_or_none_2():
    yield from (x for x in list_of_numbers if x % 2 == 0)


def test_filtering_even_numbers_or_none():
    result = next(filtering_even_numbers_or_none_1())
    for num in result:
        print(num)


def test_filtering_even_numbers_or_none_2():
    result = filtering_even_numbers_or_none_2()  # Remove list_of_numbers argument
    result_list = [*result]  # Use * operator to unpack the generator into a list
    print(result_list)
