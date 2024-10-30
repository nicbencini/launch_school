"""
Using the class definition from problem 3, let's create some more people (Person objects). Without adding any code to the Person class, 
we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?
"""

class Person:

    def __init__(self, input_name):

        self.name = input_name
    
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
rob = Person('Robert Smith')

print(bob.name == rob.name)