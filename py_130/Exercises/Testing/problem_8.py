import unittest

class SameObjectAssertions(unittest.TestCase):

    def test_same_object(self):
        self.assertIs(lst, lst.process())