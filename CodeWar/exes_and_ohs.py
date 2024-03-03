import unittest

def xo(s):
    return s.lower().count('x') == s.lower().count('o')


class TestXO(unittest.TestCase):
    def test_xo_equal_counts(self):
        # Test when 'x' and 'o' have equal counts
        self.assertTrue(xo('xo'))
        self.assertFalse(xo('XoO'))
        self.assertTrue(xo('XOXOXO'))

    def test_xo_unequal_counts(self):
        # Test when 'x' and 'o' have unequal counts
        self.assertTrue(xo('xO'))
        self.assertFalse(xo('XOo'))
        self.assertTrue(xo('XXOO'))
        self.assertFalse(xo('oOoO'))

    def test_xo_no_x_or_o(self):
        # Test when there are no 'x' or 'o' characters
        self.assertTrue(xo(''))
        self.assertTrue(xo(''))
        self.assertTrue(xo('abc'))

if __name__ == '__main__':
    unittest.main()
