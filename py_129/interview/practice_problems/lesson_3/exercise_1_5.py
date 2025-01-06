
class Person:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):

        if not isinstance(new_name, str):
            raise TypeError('Name must be a string!')
        
        elif len(new_name) == 0:
            raise ValueError('String length must be larger than one')

        self._name = new_name

linda = Person('Linda')
print(linda.name)         # Linda

linda.name = ''           # ValueError: Name must not be empty.