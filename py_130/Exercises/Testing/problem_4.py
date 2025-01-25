import unittest

class IncludedObjects(unittest.TestCase):

    def test_included(self):

        test_list = [1,2,3]

        self.assertIn('xyz', test_list)

if __name__ == '__main__':
    unittest.main()