import unittest

class NotIncluded(unittest.TestCase):

    def test_not_included(self):

        lst = [1,2,3]

        self.assertNotIn('xyz', lst)

if __name__ == '__main__':
    unittest.main()