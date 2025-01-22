class Car:

    def __init__(self):
        self._wheels = 4
        self._name = None
    
    @property
    def wheels(self):
        return self._wheels
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        
        self._name = new_name