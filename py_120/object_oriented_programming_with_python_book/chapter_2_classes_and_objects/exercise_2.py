"""
Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. 
You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.

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

my_car = Car('Kia',1988,'Blue')

print(my_car.color)
my_car.color =  'Red'
print(my_car.color)

print(my_car.model)
my_car.model = 'Landrover'
print(my_car.model)

print(my_car.year)
my_car.year = 2020
print(my_car.year)