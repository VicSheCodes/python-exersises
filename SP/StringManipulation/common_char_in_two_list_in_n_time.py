
def find_common_chars(s1, s2):
    return set([x for x in s1 if x in s2])


def test_find_common_chars():
    print(find_common_chars('hello', 'world'))
    assert find_common_chars('hello', 'lworld') == set(['l', 'o'])