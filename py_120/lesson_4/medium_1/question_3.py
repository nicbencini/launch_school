
class Animal:
    
    def speak(self, input):
        print(input)

class Cat(Animal):

    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    
    def bark(self):
        self.speak('Woof! Woof! Woof!')


le_tigre = Cat()
scamp = Dog()

le_tigre.meow()
scamp.bark()