"""
Update the code snippet below so that, when run, it produces the output as shown. 

What structure is defined by the code that you added? 

Explain the relationship between this structure and the objects instantiated on lines 3 and 4.


"""

class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    def bark(self):
        print('Woof! Woof!')


fido = Dog('Fido', 5)
paws = Dog('Paws', 3)

print(fido.name)              # Fido
print(paws.name)              # Paws
print(fido.age)               # 5
print(paws.age)               # 3

fido.bark()                   # Woof! Woof!
paws.bark()                   # Woof! Woof!

try:
    fido.name = 'Barni'
except AttributeError as e:
    print(f"Error: {e}")      # prints error message

try:
    paws.age = 4
except AttributeError as e:
    print(f"Error: {e}")      # prints error message