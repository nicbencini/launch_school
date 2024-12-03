class Cat:
    def __init__(self, name):
        self._name = name
        
    
    def greet(self):
        print(f"Hello! My name is {self._name}!")

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name


kitty = Cat('Bob')
kitty.greet()