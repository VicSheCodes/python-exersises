import functools
import time
import urllib.request
from functools import cache, lru_cache, wraps


# creating a thin wrapper around a dictionary lookup for the function arguments.
# >>> factorial(10)      # no previously cached result, makes 11 recursive calls
# 3628800
# >>> factorial(5)       # just looks up cached value result
# 120
# >>> factorial(12)      # makes two new recursive calls, the other 10 are cached
# 479001600


def measure_execution_time(func):
    total_execution_time = 0  # Variable to store the total execution time

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal total_execution_time  # Access the outer scope variable
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution time
        total_execution_time += execution_time  # Add to total execution time
        return result

    # Define a function to print the total execution time
    def print_total_execution_time():
        print(f"Total execution time of {func.__name__}: {total_execution_time:.9f} seconds")

        # Add a custom attribute to the wrapper function to print total execution time

    wrapper.print_total_execution_time = print_total_execution_time

    return wrapper


@measure_execution_time
@cache
def factorial(n):
    time.sleep(0.000000001)
    return n * factorial(n - 1) if n else 1


# @measure_execution_time
@lru_cache(maxsize=32)
def count_vowels(word):
    time.sleep(0.000000001)
    return sum(word.count(vowel) for vowel in 'AEIOUaeiou')


@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = f'https://peps.python.org/pep-{num:04d}'
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


# def test_get_pep():
#     for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
#         pep = get_pep(n)
#         print(n, len(pep))
#
#     # CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
#     print(get_pep.cache_info())
#     get_pep.cache_clear()
#     print(get_pep.cache_info())


if __name__ == '__main__':
    print(count_vowels('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
                       'The quick brown fox jumps over the lazy dog '
                       'oooooooooooooooooooooooooooooooooooooooooooo'
                       'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiaaa'))
    print(count_vowels.cache_info())
    print(count_vowels.clean())
    # print(factorial(10))
    # factorial.print_total_execution_time()
    # print(factorial(5))
    # factorial.print_total_execution_time()
    # print(factorial(12))
    # factorial.print_total_execution_time()
    # print(factorial(10))
    # factorial.print_total_execution_time()
