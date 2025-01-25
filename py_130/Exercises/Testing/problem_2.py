import unittest

class EqualityTest(unittest.TestCase):

    def test_equality(self):

        value = 'XYZ'

        self.assertEqual(value.lower(), 'xyz')

if __name__ == '__main__':
    unittest.main()