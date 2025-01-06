class Car:

    def __init__(self, model, model_year, color):
        self._model = model
        self._model_year = model_year
        self._color = color
        self._speed = 0
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color
    
    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._model_year

    def turn_engine_on(self):
        print('Enigne is on')
    
    def accelerate(self):
        self._speed += 1
        print('Car has accelerated.')
        self.get_speed()
    
    def press_break(self):
        self._speed = 0
        print('Car has stopped.')
    
    def turn_engine_off(self):
        print('Engine is off')
    
    def get_speed(self):
        print(f'Current speed is {self._speed} mph.')
    
    def spray(self, new_color):
        self.color = new_color

        print(f'The car has been sprayed {self.color}')
    
    @classmethod
    def calculate_milage(cls, distance, fuel_burned):
        milage = distance/fuel_burned

        print(f'The milage is {milage} miles per gallon')


my_car = Car('Toyota', 1989, 'red')

my_car.turn_engine_on()
my_car.accelerate()
my_car.press_break()
my_car.turn_engine_off()

print(my_car.color)
my_car.color = 'blue'

print(my_car.color)
print(my_car.year)
print(my_car.model)
my_car.spray('black')
my_car.calculate_milage(12,23)