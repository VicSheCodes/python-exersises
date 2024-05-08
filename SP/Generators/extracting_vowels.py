
word = 'hello aozoe i'


def test_extracting_vowels_1():
    generator = (char for char in word if char in 'aouei')
    for vowel in generator:
        print(vowel)


def test_extracting_vowels_2():
    generator = (char for char in word if char in 'aeiou')
    while True:
        try:
            print(next(generator))
        except StopIteration:
            break


# will print a list ['e', 'o', 'a', 'o', 'o', 'e', 'i']
def test_extracting_vowels():
    generator = (char for char in word if char in 'aeiou')
    vowels = [*generator]
    print(vowels)
