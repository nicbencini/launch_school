"""
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.
You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods.

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