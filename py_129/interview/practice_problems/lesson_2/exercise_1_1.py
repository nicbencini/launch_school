
class Person:

    def __init__(self, name):

        self._clean_name(name)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name
    
    @name.setter
    def name(self, new_name):
        self._clean_name(new_name)


    def _clean_name(self, input_name):

        if ' ' in input_name:
            name_list = input_name.split(' ')
            self._first_name = name_list[0]
            self._last_name = name_list[1]
        
        else:
            self._first_name = input_name
            self._last_name = ''

    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name


bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams