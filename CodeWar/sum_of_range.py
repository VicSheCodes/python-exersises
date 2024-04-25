'''
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.

'''


def get_sum_long(a, b):
    summary = 0
    if a == b:
        return a
    if a < b:
        summary = a
        for i in range(a, b):
            if i == 0 or i == a:
                continue
            summary += i
        summary += b
    elif a > b:
        summary = b
        for i in range(b, a):
            if i == 0 or i == b:
                continue
            summary = + i
        summary += a
    return summary


def get_sum_2(a, b):
    start, end = min(a, b), max(a, b)
    return sum(range(start, end)) + end


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def test_get_sum():
    assert get_sum(1, 0) == 1
    assert get_sum(1, 2) == 3
    assert get_sum(0, 1) == 1
    assert get_sum(1, 1) == 1
    assert get_sum(-1, 0) == -1
    assert get_sum(-1, 2) == 2
