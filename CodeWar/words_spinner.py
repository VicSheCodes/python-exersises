sentnences = ["Hey fellow warriors", "This is a test", "This is another test", "", "     hi", "Words", "sdroW"]
#
# def words_spinner(sentence):
#     words = [word[::-1] if len(word) >=5 else word for word in sentence.split(' ')]
#     return ' '.join(words)
#


import unittest

def words_spinner(sentence):
    words = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return ' '.join(words)

if __name__ == '__main__':
    print("This code will only run if the script is executed directly, not when imported as a module.")
    for sentence in sentnences:
        print(words_spinner(sentence))


class TestWordsSpinner(unittest.TestCase):
    def test_words_spinner_reverses_long_words(self):
        # Test that the function reverses words longer than or equal to 5 characters
        self.assertEqual(words_spinner("Hey fellow warriors"), "Hey wollef sroirraw")

    def test_words_spinner_does_not_reverse_short_words(self):
        # Test that the function does not reverse words shorter than 5 characters
        self.assertEqual(words_spinner("This is a test"), "This is a test")

    def test_words_spinner_handles_empty_string(self):
        # Test that the function handles an empty string
        self.assertEqual(words_spinner(""), "")

    def test_words_spinner_handles_spaces(self):
        # Test that the function handles leading and trailing spaces
        self.assertEqual(words_spinner("     Words    "), "sdroW")

    def test_words_spinner_handles_single_word(self):
        # Test that the function handles a single word
        self.assertEqual(words_spinner("sdroW"), "Words")

if __name__ == '__main__':
    unittest.main()
