

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def test_fibonacci():
    fibonacci_generator = fibonacci()
    # for _ in range(30):
    #     print(next(fibonacci_generator))

    fib_list = [str(next(fibonacci_generator)) for _ in range(30)]
    print("\n", *fib_list)

    print(*fib_list)
    print(f"\n {' '.join(map(str, fib_list))} ")

    print("\n", ', '.join(fib_list))