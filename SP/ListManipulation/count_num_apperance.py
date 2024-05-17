
def count_num_appearance(arr, num):
    return arr.count(num)


if __name__ == "__main__":
    print(count_num_appearance([1, 2, -4, 3, 4, 5, 41, 4], 4))


def test_count_num_appearance():
    assert count_num_appearance([1, 2, -4, 3, 4, 5, 41, 4], 4) == 2
    assert count_num_appearance([1, 2, -4, 3, 4, 5, 41, 4], 3) == 1