# URLify


def replace_spaces(string):
    return string.strip().replace(' ', "%20")


def test_replace_string():
    assert replace_spaces("  hello world ") == "hello%20world"
    assert replace_spaces("hello") == "hello"
    assert replace_spaces("") == ""
    assert replace_spaces(" ") == ""
    assert replace_spaces("  ") == ""
    assert replace_spaces("  a ") == "a"