
class Car:

    def __init__(self, type, year, color):
        self._type = type
        self._year = year
        self._color = color
    
    def __str__(self):
        return f'{self._color} {self._year} {self._type}'
    
    def __repr__(self):
        return f'Car(\'{self._type}\', {self._year}, \'{self._color}\')'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')