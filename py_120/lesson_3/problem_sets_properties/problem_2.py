class Person:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):

        if not isinstance(new_name, str):
            raise TypeError('Input must be string')
        
        if len(new_name) == 0:
            raise ValueError('Strings must not be empty')
        
        self._name = new_name
    

person_1 = Person('Jack')

print(person_1.name)

person_1.name = 'Jill'

print(person_1.name)

person_1.name = ''

print(person_1.name)