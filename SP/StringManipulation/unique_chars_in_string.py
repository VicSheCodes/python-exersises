

def find_string_with_unique_chars(string):
    # for char in string:
    #     if string.count(char) != 1:
    #         return
    # yield string

    if all(string.count(chr) == 1 for chr in string):
        yield string


if __name__ == "__main__":
    list_of_strings = ["abbbaac", "d", "ghost", "jjj", "", ]

    # for str in list_of_strings:
    #     print(*(find_string_with_unique_chars(str)))

    for str in list_of_strings:
        result = next(find_string_with_unique_chars(str), None)
        if result:
            print(result)


