words = ["hello", "world"]


def generator_function():
    for word in words:
        yield word.upper()


def test_tansform_every_string_in_the_list_to_upper():
    print(f"\n")
    print(*(generator_function()))
    print([*(generator_function())])
    generator = generator_function()
    while True:
        try:
            transformd_word = next(generator)
            print(transformd_word)
        except StopIteration:
            break
