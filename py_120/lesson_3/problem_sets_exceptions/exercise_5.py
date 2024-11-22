
class NegativeNumberError(Exception):

    def __init__(self, message = 'Number must not be negative!'):
        super().__init__(message)


number = float(input('Please input a number: '))

if number < 0:
    raise NegativeNumberError()

print(f'You entered {number}')