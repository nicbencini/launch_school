class Person:
    def __init__(self, name, weight, height):
        self._name = name
        self._weight = weight
        self._height = height
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def weight(self):
        return self._weight
    
    @ weight.setter
    def weight(self, new_weight):
        self._weight = new_weight
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        self._height = new_height
    
    

susan = Person('susan', 123, 64)
print(f'{susan.name} {susan.weight} {susan.height}')
# susan 123 64

susan.name = susan.name.capitalize()
susan.weight += 2
susan.height += 0.5

print(f'{susan.name} {susan.weight} {susan.height}')
# Susan 125 64.5