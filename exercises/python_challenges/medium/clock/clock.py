"""
Create a clock that is independent of date.

You should be able to add minutes to and subtract minutes from the time represented by a given Clock object. 
Note that you should not mutate Clock objects when adding and subtracting minutes -- create a new Clock object.

Two clock objects that represent the same time should be equal to each other.

You may not use any built-in date or time functionality; just use arithmetic operations.

problem:
create a clock that allows you to add minutes and subtract minutes from the time represented by a given Clock object

rules:
- clock objects should not be mutated when adding and subtracting minutes, new objects should be created
- two clock objects that represent the same time should be equal to each other

data:
    -Clock(class):
        - initialize (hours, minuts = 0)
        - at (method) - sets clock to a specific time
        - __add__ - allows the addition on integers to clock
        - __sub__ - allows the subtraction of integers from clock
        - __eq___ - compare equivalent clocks

algorithm:
    - create variable for hours and minutes
        - if minutes is greater than 60, hours + 1
        - if minutes is less than 0 hours - 1

        if hours is greater than 23 then hours wrap around
        if hours is less than 0 then hours wrap around: 
            - 23hours + 100 min
            - convert 100 min into equivalent hours = 100/60 = 1.6
            - 23 + 1.6 % 24 = 0.6 = 0.6*60 = 40 min
            - time us 0 hours 40 min

            - 1:00 - 122 minutes
            - convert 122 minutes to hours = 2hours
            - if there is a remainder subtract another hour
            1:00 - 3hours == -2hours
            - if result is smaller than 0:
                24hours - result = 22hours
            60min - remainder = 58min
"""

class Clock:

    def __init__(self, hours, minutes):

        
        self._hours = hours
        self._minutes = minutes


    @classmethod
    def at(cls, hours, minutes=0):

        return cls(hours, minutes)

        
    def __str__(self):
        return f'{self._hours:02d}:{self._minutes:02d}'
    
    def __repr__(self):
        return f'{self._hours:02d}:{self._minutes:02d}'
    
    def __add__(self, other):

        hours = (self._hours + (other//60)) % 24
        minutes = (self._minutes + other) % 60

        return Clock.at(hours, minutes)
    
    def __sub__(self, other):

        hours = self._hours - (other//60)%24
        minutes = self._minutes - (other % 60)

        if minutes < 0:
            minutes = 60 + minutes
            hours -= 1
        
        if hours < 0:
            hours = 24 + hours

        return Clock.at(hours, minutes)
    
    def __eq__(self,other):

        if str(self) == str(other):
            return True



