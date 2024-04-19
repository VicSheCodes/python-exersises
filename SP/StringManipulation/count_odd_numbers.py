'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''


def find_odd_number(arr):
    numbers_count = {}
    for num in arr:
        numbers_count[num] = numbers_count.get(num, 0) + 1
    print(numbers_count)
    return (k for k, v in numbers_count.items() if v % 2 != 0)


def find_odd_number_2(arr):
    # Count occurrences of each number using a dictionary comprehension
    numbers_count = {num: arr.count(num) for num in arr}

    # Return a generator expression containing keys where values are odd
    return (k for k, v in numbers_count.items() if v % 2 != 0)


def test_find_odd_number():
    assert next(find_odd_number([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])) == 4
    assert (next(find_odd_number([0, 1, 0, 1, 0]))) == 0
    assert next(find_odd_number_2([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])) == 4


if __name__ == "__main__":
    print(*(find_odd_number([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])))

