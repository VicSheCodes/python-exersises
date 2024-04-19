import math


def count_trailing_zeros_in_factorial(n):
    if n <= 0:
        return 0

    max_k = math.floor(math.log(n, 5))
    trailing_zeros = sum(n // (5 ** k) for k in range(1, max_k + 1))
    return trailing_zeros

def zeros(n):
    count = 0
    while n:
        n = n // 5
        count += n
    return count

def test_count_trailing_zeros_in_factorial():
    assert zeros(5) == 1
    assert count_trailing_zeros_in_factorial(6) == 1
    assert count_trailing_zeros_in_factorial(7) == 1
    assert zeros(8) == 1
    assert zeros(9) == 1
    assert zeros(10) == 2
    assert count_trailing_zeros_in_factorial(11) == 2
    assert count_trailing_zeros_in_factorial(12) == 2
    assert count_trailing_zeros_in_factorial(13) == 2
    assert count_trailing_zeros_in_factorial(15) == 3
    assert zeros(20) == 4