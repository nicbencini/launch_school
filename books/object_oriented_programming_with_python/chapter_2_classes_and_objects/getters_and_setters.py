
class dog:

    def __init__ (self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        print(f'{self._name} says woof!')
    
    def name(self):
        return self._name

    def set_name(self, new_name):

        if not isinstance(new_name,str):
            raise TypeError('Input is not string')

        self._name = new_name


class cat:

    Owner = 'Nicolo'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'{self.name} says meow!')

    @classmethod
    def belongs_to(cls):
        print(f'This cat belongs to {cls.Owner}')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    



dog_1 = dog('Scamp', 8)
cat_1 = cat('Tigre', 9)

cat_1._name = 'bob'

cat_1.name = 'Le Tigre'

cat_1.belongs_to()


#dog_1.name = 'Fido'
dog_1.set_name('Buzz')

print(dog_1.name())

dog_1.speak()
cat_1.speak()

