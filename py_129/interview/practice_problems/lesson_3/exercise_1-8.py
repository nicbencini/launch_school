class Dog:

    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed
    
    breed.setter
    def breed(self, new_breed):
        self._breed = new_breed
    
    def get_breed(self):
        print(f'{self.breed}')

class Cat:

    def __init__(self):
        pass

    def get_name(self):
        if not hasattr(self,'name'):
            print('Name not set!')
        else:
            print(self.name)
    
dog_1 = Dog('Golden Retreiver')
dog_2 = Dog('Poodle')

dog_1.get_breed()
dog_2.get_breed()

cat_1 = Cat()
cat_1.get_name()
cat_1.name = 'test'
cat_1.get_name()