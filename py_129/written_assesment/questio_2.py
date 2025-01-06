
class Vehicle:

    def __init__(self):
        pass
        
    def start(self):
        pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass


class ColorMixin:
    def set_color(self):
        pass

class Car(ColorMixin):
    pass

class Plane(ColorMixin):
    pass