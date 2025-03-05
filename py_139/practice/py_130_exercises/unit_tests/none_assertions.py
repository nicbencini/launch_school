"""
Write a unittest assertion that will fail if value is not None.
"""

import unittest

value = 'test'

class NoneAssertion(unittest.TestCase):

    def test_none_assertion(self):
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()