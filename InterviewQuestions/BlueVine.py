# Given an array containing None values, fill in the None values with the most recent
# non None value in the array.
# For example, for array1= [1, None, 2, 3, None, None, 5, None]
# Output should be: [1, 1, 2, 3, 3, 3, 5, 5]

def refill_array(list_with_nones):
    current_non_none_value = None
    for i in range(0, len(list_with_nones)):
        if list_with_nones[i] is not None:
            current_non_none_value = list_with_nones[i]
        else:
            list_with_nones[i] = current_non_none_value

    return list_with_nones


def pythonic_refill_array(list_with_nones):
    current = None
    return [current if element is None else (current := element) for element in list_with_nones]


if __name__ == "__main__":
    print(refill_array([1, None, 2, 3, None, None, 5, None]))
    print(pythonic_refill_array([1, None, 2, 3, None, None, 5, None]))
