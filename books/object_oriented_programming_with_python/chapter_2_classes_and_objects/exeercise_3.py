"""
Add a method to the Car class that lets you spray paint the car a specific color. 
Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.
"""

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

        self.speed = 0
        self.engine = False

    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):

        if not isinstance(color, str):
            raise TypeError('Input not of type string')

        self._color = color
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self,model):
        
        if not isinstance(model, str):
            raise TypeError('Input not string')

        self._model = model
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):

        if not isinstance(year, int):
            raise TypeError('Input not integer')
        
        self._year = year

    def turn_on_engine(self):
        self.engine = True
        print('Engine is on!')
    
    def turn_off_engine(self):
        self.engine = False
        self.speed = 0
        print('Engine is off!')
    
    def accelerate(self):
        if self.engine == False:
            print('Turn on Engine First!')
        else:
            self.speed += 1
    
    def press_break(self):
        if self.speed > 0:
            self.speed -= 1
        
        
    def get_speed(self):
        print(f'The speed is {self.speed} mph')

    def spray(self,color):
        self.color = color

        print(f'Your car has been spayed {self.color}')

my_car = Car('Kia',1988,'Blue')

print(my_car.color)

my_car.spray('Yellow')

print(my_car.color)

