"""
Going back to your solution to exercise 1, refactor the code to replace any methods that can be converted to static methods. 
Once you have done that, ask yourself whether the conversion to a static method makes sense.
"""

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

        self.speed = 0
        self.engine = False
    
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

my_car = Car('Kia','1989','Silver')
my_car.turn_on_engine()
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.get_speed()
my_car.press_break()
my_car.get_speed()
my_car.turn_off_engine()
my_car.get_speed()
my_car.accelerate()