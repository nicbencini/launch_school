class GoodDog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

sparky = GoodDog('Sparky', 5)

sparky._name = 'Fido'
print(sparky._name)         # Fido
print(sparky.speak())        # Sparky says arf!

