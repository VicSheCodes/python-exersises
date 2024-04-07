lst = [6, 9, 2, 4, 1, 9, 2, 1, 7]


def calculate_second_largest(lst):
    cur_max = 0
    second_max = 0

    lst = list(set(lst))
    for item in range(len(lst)):
        if lst[item] > cur_max:
            second_max = cur_max
            cur_max = lst[item]
        elif lst[item] > second_max:
            second_max = lst[item]

    return second_max


# Writing a function to find the kth largest element in a list involves creating an algorithm
# that efficiently determines the kth largest value in the list, regardless of whether
# the list is sorted or unsorted.


def finds_kth_largest(lst, k):
    if not lst or k < 1 or k > len(lst):
        return None

    sorted_lst = sorted(set(lst), reverse=True)

    return sorted_lst[k - 1]


if __name__ == '__main__':
    print(calculate_second_largest(lst))
    print(finds_kth_largest(lst, 2))
