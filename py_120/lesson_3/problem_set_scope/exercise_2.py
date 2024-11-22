class Dog:

    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog_1 = Dog('Golden Retriever')
dog_2 = Dog('Poodle')

print(dog_1.get_breed())
print(dog_2.get_breed())