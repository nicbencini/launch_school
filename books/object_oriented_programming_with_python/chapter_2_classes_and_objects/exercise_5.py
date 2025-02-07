"""
Create a Person class with two instance variables to hold a person's first and last names. 
The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), 
with both first and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

"""

class Person:

    @classmethod
    def is_alphabetic(cls, input_string):

        if not isinstance(input_string,str):
            raise TypeError('Input must be string.')
        elif len(input_string) == 0:
            return False
        else:
            return all([character.isalpha() for character in input_string])

    def __init__(self, first_name, second_name):

        if not (self.is_alphabetic(first_name) and self.is_alphabetic(second_name)):
            raise ValueError('Name must be alphabetic')

        self.first_name = first_name
        self.second_name = second_name
        
    @property
    def name(self):
        return f'{self.first_name.title()} {self.second_name.title()}'
    
    @name.setter
    def name(self, name_tuple):

        if not (self.is_alphabetic(name_tuple[0]) and self.is_alphabetic(name_tuple[1])):
            raise ValueError('Name must be alphabetic')

        self.first_name = name_tuple[0]
        self.second_name = name_tuple[1]


"""
actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
print(actor.name)   
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.
"""
friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.
