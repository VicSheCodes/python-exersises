'''
Count Vowels and Consonants:
Write a function that takes a string as input and returns the count of vowels and consonants in the string separately.
'''


def count_vowels_and_consonants(words):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels_count = 0
    consonants_count = 0

    for letter in words:
        if letter.lower() in vowels:
            vowels_count += 1
        elif letter.lower() in consonants:
            consonants_count += 1
    return vowels_count, consonants_count


def test_count_vowels_and_consonants():
    assert count_vowels_and_consonants('hello') == (2, 3)
    assert count_vowels_and_consonants('hello world') == (3, 7)
    assert count_vowels_and_consonants('') == (0, 0)
    assert count_vowels_and_consonants('a') == (1, 0)
    assert count_vowels_and_consonants('hel2lo w8orld!') == (3, 7)

