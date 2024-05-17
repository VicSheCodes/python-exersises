"""
Fibonacci Series using Recursion.
The Fibonacci numbers are the numbers in the following integer sequence:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……

"""
import pytest


def fibonacci_sum(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sum(n - 1) + fibonacci_sum(n - 2)


def print_fibonacci_series(n):
    result = []
    for i in range(n):
        result.append(fibonacci_sum(i))
    print("\n", result)


def calculate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci_generator = calculate_fibonacci()
    fib_list = [next(fibonacci_generator) for _ in range(10)]
    print("\n", *fib_list)
    print("\n", fib_list)

    print_fibonacci_series(5)

    pytest.main([__file__])


def test_fibonacci_sum():
    assert fibonacci_sum(5) == 5
    assert fibonacci_sum(10) == 55
