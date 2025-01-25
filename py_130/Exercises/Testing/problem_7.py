import unittest

class Numeric:

    def __init__(self):
        pass

class TypeAssertions(unittest.TestCase):

    def setUp(self):
        self.test_object = Numeric()

    def test_type_assertions(self):

        self.assertIsInstance(self.test_object, Numeric)

if __name__ == '__main__':
    unittest.main()

