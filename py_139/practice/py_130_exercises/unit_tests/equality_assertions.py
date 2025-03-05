"""
Write a unittest assertion that will fail if value.lower does not return 'xyz'.
"""

import unittest

value ='Xyz'

class Equality_Assertions(unittest.TestCase):

    def test_equality_assertion(self):
        self.assertEqual(value.lower(), 'xyz')

if __name__ == '__main__':
    unittest.main()