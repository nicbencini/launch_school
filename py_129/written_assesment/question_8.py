
class Car:
    def __init__(self, speed):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def accelerate(self):
        new_speed = self.speed + 10
        self.speed = new_speed

    def is_faster_than(self, other_car):
        return self.speed > other_car.speed

# Testing the Car class
car1 = Car(40)
car2 = Car(40)
car1.accelerate()
print(car1.is_faster_than(car2))