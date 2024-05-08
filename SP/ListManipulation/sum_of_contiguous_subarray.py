
def sum_of_contiguous_subarray(arr, k):
    """
    :param arr: list of integers
    :param k: integer
    :return: sum of the contiguous subarray with length k
    """
    if len(arr) < k:
        return 0
    return sum(arr[:k])

