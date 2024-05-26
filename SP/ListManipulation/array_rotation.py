
def is_there_a_rotation1(list1, list2):
    if len(list1) != len(list2):
        return False

    concatenated_list = list1+list1

    str2 = ''.join(map(str, list2))
    str_concatinated = ''.join(map(str, concatenated_list))

    return str2 in str_concatinated


def is_there_a_rotation_no_string_converting(list1, list2):
    if len(list1) != len(list2):
        return False

        # Concatenate list1 with itself
    concatenated_list = list1 + list1

    # Debug: Print concatenated list
    print(f"Concatenated List: {concatenated_list}")

    # Check if list2 is a sublist of the concatenated list
    for i in range(len(list1)):
        # Debug: Print the sublist being compared
        print(f"Comparing {concatenated_list[i:i + len(list2)]} with {list2}")
        if concatenated_list[i:i + len(list2)] == list2:
            return True

    return False


def test_is_there_a_rotation():
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 1, 2]
    assert (is_there_a_rotation(l1, l2)) is True

    l3 = [1, 2, 3, 4, 5]
    l4 = [4, 5, 1, 2, 3]
    assert (is_there_a_rotation(l3, l4)) is True

    l5 = [1, 2, 3, 4, 5]
    l6 = [5, 4, 3, 2, 1]
    assert (is_there_a_rotation(l5, l6)) is False

    l7 = [1, 2, 3, 4, 5]
    l8 = [1, 2, 3, 4]
    assert (is_there_a_rotation(l7, l8)) is False



