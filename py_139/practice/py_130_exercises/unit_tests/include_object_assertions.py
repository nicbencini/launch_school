"""
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.
"""
import unittest

lst = ['yx','xyz']

class IncludeObjectAssertions(unittest.TestCase):

    def test_include_object(self):
        self.assertIn('xyz', lst)

if __name__ == '__main__':
    unittest.main()