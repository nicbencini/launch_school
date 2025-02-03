import unittest

class NotNone(unittest.TestCase):

    def test_none(self):

        value = 'test'

        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()