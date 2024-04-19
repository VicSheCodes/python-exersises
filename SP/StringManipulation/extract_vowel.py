'''

Write a function that takes a string as input and returns the same string with all vowels removed.
'''
import pytest
import unicodedata


def extract_vowels_from_string(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    normalized_words = unicodedata.normalize('NFD', words)
    return ''.join(c for c in normalized_words if c.lower() not in vowels)


@pytest.mark.parametrize("word, expected", [
    ("here comes the sun", "hr cms th sn"),
    ("",""),
    ("qwrtp", "qwrtp"),
    ("aeiou", ""),
    ("HeLLO", "HLL"),
    ("a1b2c3", "1b2c3"),
    ("hello!@#a$%o^&*()", "hll!@#$%^&*()"),
    ("cáfé", "cf")
])
def test_extract_vowels_from_string(word, expected):
    assert extract_vowels_from_string(word) == expected



