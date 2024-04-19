import pytest


def anagrams(word1, word2):
    a = ''.join(sorted(word1))
    b = ''.join(sorted(word2))
    return a == b


@pytest.mark.parametrize("word_1, word_2", [('racer', 'craer'), ('carer', 'recar'), ('caers', 'races')])
def test_anagrams(word_1, word_2):
    assert anagrams(word_1, word_2) == True


def anagrams_list(word, words):
    sorted_word = ''.join(sorted(word))
    result_list = []
    for w in words:
        if sorted_word == ''.join(sorted(w)):
            result_list.append(w)
    return (result_list)

def anagrams_list_comprehension(word, words):
    sorted_word = ''.join(sorted(word))
    return [w for w in words if ''.join(sorted(w)) == sorted_word]


@pytest.mark.parametrize("word, words, expected", [
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab'], ['aabb', 'bbaa']),
    ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer']),
    ('laser', ['lazing', 'lazy', 'lacer'], []),
    ('a', ['a', 'b', 'c', 'd'], ['a']),
    ('big', ['gig', 'dib', 'bid', 'biig'], []),
    ('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer'], ['ab', 'ba']),
    ('abba',
     ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'],
     ['aabb', 'bbaa', 'abab', 'baba', 'baab']),
])
def test_example_tests(word, words, expected):
    result = anagrams_list(word, words)
    assert expected == result, f"Expected {expected}, but got {result} for word: {word} and words: {words}"



