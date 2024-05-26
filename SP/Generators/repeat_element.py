
def repeat_element(element, limit):
    for _ in range(limit):
        yield element


def repeat_elements(elements, times):
    for element in elements:
        for _ in range(times):
            yield element


if __name__ == "__main__":
    lst = [5, 6, 7, 8, 9, 10]
    for item in lst:
        print(*(repeat_element(item, 3)))

    for item in repeat_elements([1, 2, 3], 3):
        print(item)
