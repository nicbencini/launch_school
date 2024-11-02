"""
Create a class named Cat that prints a greeting when the greet instance method is invoked. 
The greeting should include the name and color of the cat. Use a class constant to define the color.
"""

class Cat:

    COLOR = 'purple'

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def greet(self):
        print(f'Hello! My name is {self.name} and I\'m a {self.COLOR} cat!')

    
kitty = Cat('Sophie')
kitty.greet()
