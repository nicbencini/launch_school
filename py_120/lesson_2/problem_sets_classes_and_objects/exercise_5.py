"""
Continuing with our Person class definition, what do you think the following code prints?

Let's override the str function for Person objects by defining a magic method, __str__, in the Person class:
"""

class Person:

    def __init__(self, input_name):

        self.name = input_name

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()
    
    @name.setter
    def name(self, name):

        name_parts = name.split()
        
        self.first_name = name_parts[0]
        self.last_name = ''

        if len(name_parts) > 1:
            self.last_name = name_parts[1]
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self,first_name):
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,last_name):
        self._last_name = last_name


bob = Person('Robert Smith')
print(f"The person's name is: {bob}")