list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']


# (1, 'a') (1, 'b') (1, 'c') (2, 'a') (2, 'b') (2, 'c') (3, 'a') (3, 'b') (3, 'c')
# yield
def generator_func_1():
    for x in list1:
        for y in list2:
            yield x, y


# (1, 'a') (1, 'b') (1, 'c') (2, 'a') (2, 'b') (2, 'c') (3, 'a') (3, 'b') (3, 'c')
# yield from
def generator_func_2():
    yield from ((x, y) for x in list1 for y in list2)


# different output (1, 'a') (2, 'b') (3, 'c')
def using_zip():
    yield from zip(list1, list2)


def test_combining_lists():
    print(*(generator_func_1()))
    print(*(generator_func_2()))
    print(*(using_zip()))
