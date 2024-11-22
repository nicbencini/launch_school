class Dog:

    def __init__(self, breed):
        self.breed = breed
    
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed

    def get_breed(self):
        return self.breed

dog_1 = Dog('Golden Retriever')
dog_2 = Dog('Poodle')

dog_1.breed = 'Labrador'

print(dog_1.get_breed())
print(dog_2.get_breed())