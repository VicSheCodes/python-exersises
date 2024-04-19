def array_diff_no_duplications(arr1, arr2):
    result = list(set(arr1) - set(arr2))
    return result


def array_diff_with_duplications(arr1, arr2):
    return {item for item in arr1 if item not in arr2}


if __name__ == '__main__':
    # Test with two empty arrays
    assert array_diff_no_duplications([], []) == []

    # Test with one empty array
    assert array_diff_no_duplications([1, 2, 3], []) == [1, 2, 3]

    # Test with two arrays with different values
    assert array_diff_no_duplications([1, 2, 3], [4, 5, 6]) == [1, 2, 3]

    # Test with overlapping values
    assert array_diff_no_duplications([1, 2, 3, 2,
                                       1], [2, 3]) == [1]

    # Test with one array containing all values
    assert array_diff_no_duplications([1, 2, 3], [1, 2, 3, 4, 5]) == []

    # Test with two empty arrays
    assert array_diff_with_duplications([], []) == []

    # Test with one empty array
    assert array_diff_with_duplications([1, 2, 3], []) == [1, 2, 3]

    # Test with two arrays with different values
    assert array_diff_with_duplications([1, 2, 3], [4, 5, 6]) == [1, 2, 3]

    # Test with overlapping values
    assert array_diff_with_duplications([1, 2, 3, 2, 1], [2, 3]) == [1]

    # Test with one array containing all values
    assert array_diff_with_duplications([1, 2, 3], [1, 2, 3, 4, 5]) == []
