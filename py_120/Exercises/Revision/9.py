class Cat:

    COLOR = 'Red'

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I\'m a {self.COLOR} cat')


kitty = Cat('Sophie')
kitty.greeting()
        