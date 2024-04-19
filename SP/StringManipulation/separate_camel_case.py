'''

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

import re


def separate_camel_1(s):
    if not s:
        return s

    result = [s[0]]
    for c in s[1:]:
        if c.isupper():
            result.append(' ')
        result.append(c)
    return ''.join(result)


def separate_camel_2(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


def separate_camel(s):
    return re.sub('([A-Z])', r' \1', s)



def test_separate_camel():
    assert separate_camel("camelCasing") == "camel Casing"
    assert separate_camel("identifier") == "identifier"
    assert separate_camel("") == ""
    assert separate_camel("XXX") == "X X X"
    assert separate_camel("S") == "S"
