class Animal:

    def __init__(self):
        pass

    def speak(self, sound):
        print(sound)

class Cat(Animal):

    def meow(self):
        self.speak('Meow')

class Dog(Animal):

    def bark(self):
        self.speak('Woof')


dog = Dog()
dog.bark()