'''
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
'''


def get_middle(word="wo512fa216ds"):
    print(len(word) // 2, len(word) % 2, word)


# divmod(10, 3) output: (3, 1), because 10 // 3 = 3 and 10 % 3 = 1
def get_middle_2(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


def test_get_middle_3(s = "mabboovvth"):
    i = (len(s) - 1) // 2
    print(len(s))
    print(i)
    print(s[i:-i] or s)
