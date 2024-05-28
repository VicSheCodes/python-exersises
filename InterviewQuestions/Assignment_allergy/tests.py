import unittest
from solution import allergies, is_allergic_to

class TestIsAllergicTo(unittest.TestCase):
    def test_false_on_untracked_allergy(self):
        """ should return false for an untracked allergy """
        self.assertFalse(is_allergic_to(3, "foobar"))
    
    def test_basic_tests(self):
        """ should work on basic tests """
        self.assertFalse(is_allergic_to(0, "peanuts"))
        self.assertFalse(is_allergic_to(0, "cats"))
        self.assertFalse(is_allergic_to(0, "strawberries"))
        self.assertTrue(is_allergic_to(1, "eggs"))
        self.assertTrue(is_allergic_to(2, "peanuts"))
        self.assertTrue(is_allergic_to(5, "eggs"))
        self.assertTrue(is_allergic_to(5, "shellfish"))
        self.assertFalse(is_allergic_to(5, "strawberries"))

class TestAllergies(unittest.TestCase):
    def test_basic_tests(self):
        """ should work on basic tests """
        self.assertEqual(allergies(0), [])
        self.assertEqual(allergies(2), ["peanuts"])
        self.assertEqual(allergies(6), ["peanuts", "shellfish"])
        self.assertEqual(allergies(255), ["cats", "chocolate", "eggs", "peanuts", "pollen", "shellfish", "strawberries", "tomatoes"])
        self.assertEqual(allergies(256), [])
        self.assertEqual(allergies(257), ["eggs"])
        self.assertEqual(allergies(258), ["peanuts"])
        self.assertEqual(allergies(259), ["eggs", "peanuts"])
        self.assertEqual(allergies(260), ["shellfish"])
        self.assertEqual(allergies(1000), ["cats", "chocolate", "pollen", "strawberries"])
