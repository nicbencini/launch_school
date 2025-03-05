"""
Write a unittest assertion that will fail if value % 2 != 0 is not True.
"""

import unittest

value = 4

class BooleanAssertion(unittest.TestCase):

    def test_bool_assertion(self):

        self.assertTrue(value % 2 != 0)

if __name__ == '__main__':
    unittest.main()