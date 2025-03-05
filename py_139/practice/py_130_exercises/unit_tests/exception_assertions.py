import unittest

class ExceptionsAssertions(unittest.TestCase):

    def test_exception(self):

        with self.assertRaises(NoExperienceError):
            employee.hire()

if __name__ == '__main__':
    unittest.main()