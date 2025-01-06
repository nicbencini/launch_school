class Animal:
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        self.speak('Meow')

class Dog(Animal):
    def bark(self):
        self.speak('Woof')
