
class Vehicle:

    seat = 4

    def __init__(self, wheels):
        self._wheels = wheels
        windows = 2
    
    @classmethod
    def driver(cls):
        print(cls.seat)

        
