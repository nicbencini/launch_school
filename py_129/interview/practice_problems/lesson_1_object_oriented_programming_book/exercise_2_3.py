class Person:

    def __init__(self, first_name, last_name):

        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError('Name must be alphabetic')
        
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def name(self):
        return(f'{self._first_name.title()} {self._last_name.title()}')
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, tuple) and len(new_name) != 2:
            raise TypeError('Input must be Tuple with 2 strings')
        
        if not new_name[0].isalpha() or not new_name[1].isalpha():
            raise ValueError('Name must be alphabetic')
        
        self._first_name = new_name[0]
        self._last_name = new_name[1]



friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.
