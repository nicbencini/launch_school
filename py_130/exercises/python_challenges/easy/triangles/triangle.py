
class Triangle:

    def __init__(self, side_1, side_2, side_3):
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

        if (self._side_1 <= 0 or 
            self._side_2 <= 0 or 
            self._side_3 <= 0):

            raise ValueError('Triangle sides must be greater than zero!')
        
        if ((self._side_1 + self._side_2 <= self._side_3) or
            (self._side_2 + self._side_3 <= self._side_1) or
            (self._side_3 + self._side_1 <= self._side_2)):

            raise ValueError('Invalid triangle!')

    @property
    def kind(self):

        if self.is_equilateral():
            return 'equilateral'
        elif self.is_scalene():
            return 'scalene'
        else:
            return 'isosceles'
    
    def is_equilateral(self):
        if (self._side_1 == self._side_2 and 
            self._side_2 == self._side_3):
            return True
        
        return False
    
    def is_scalene(self):
        if (self._side_1 != self._side_2 and 
            self._side_2 != self._side_3 and
            self._side_1 != self._side_3):
            return True
        
        return False