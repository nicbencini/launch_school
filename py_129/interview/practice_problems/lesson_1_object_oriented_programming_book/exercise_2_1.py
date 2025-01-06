class Car:

    def __init__(self, model, model_year, color):
        self._model = model
        self._model_year = model_year
        self._color = color
        self._speed = 0
    
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


my_car = Car('Toyota', 1989, 'red')

my_car.turn_engine_on()
my_car.accelerate()
my_car.press_break()
my_car.turn_engine_off()