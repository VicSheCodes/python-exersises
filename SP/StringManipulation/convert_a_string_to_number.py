def convert_a_string_to_number(word):
    n = len(word)
    if n == 0:
        return None
    elif word[0] == '-':
        return -convert_a_string_to_number(word[1:])
    return sum((int(s) * 10 ** (n - i - 1) for i, s in enumerate(word)))


def string_to_number(s):
    return int(s)


def convert_a_string_to_number_generator(word):
    n = len(word)
    yield (int(s) * 10 ** (n - i - 1) for i, s in enumerate(word))


if __name__ == "__main__":
    for digit in convert_a_string_to_number_generator("12345"):
        print(sum(digit))
    print(string_to_number("123456"))