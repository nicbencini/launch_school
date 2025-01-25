import unittest

class TestClass(unittest.TestCase):

    def test_boolean(self):

        value = 4

        self.assertTrue(value % 2 != 0, 'Value is not odd')

if __name__ == '__main__':
    unittest.main()