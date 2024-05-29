import pandas as pd
import unittest

import analysis

class Test(unittest.TestCase):
    def test_analyze(self):
        """ Test obesity rates of the most populous countries """
        actual = analysis.analyze("data/c2119.csv", "data/c2228.csv")
        expected = pd.read_csv("data/result.csv")
        expected.index += 1
        pd.testing.assert_frame_equal(actual, expected)
