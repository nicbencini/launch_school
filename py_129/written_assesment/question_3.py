class ShoutMixin:
    def speak(self):
        print("I'M SHOUTING!!!")

class WhisperMixin:
    def speak(self):
        print("i'm whispering....")

class Person:
    def speak(self):
        print("I'm speaking.")

class Child(WhisperMixin, ShoutMixin, Person):
    pass

Child().speak()