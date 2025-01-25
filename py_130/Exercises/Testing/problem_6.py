import unittest

class NoExperienceError(Exception):

    def __init(self, message="No Experience!"):
        super().__init__(message)

class Employee:

    def __init__(self):
        pass
    

    def hire(self):

        raise NoExperienceError

class ExceptionAssertions(unittest.TestCase):

    def setUp(self):
        self.employee = Employee()

    def test_exception(self):
        
        while self.assertRaises(Exception):
            self.employee.hire()

if __name__ == '__main__':
    unittest.main()

