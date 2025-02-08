"""
Write a program that manages robot factory settings.

When robots come off the factory floor, they have no name. The first time you boot them up, a random name is generated, such as RX837 or BC811.

Every once in a while, we need to reset a robot to its factory settings, which means that their name gets wiped. The next time you ask, it will respond with a new random name.

The names must be random; they should not follow a predictable sequence. Random names means there is a risk of collisions. Your solution should not allow using the same name twice.

problem:
 -write a program that assings robot names

rules:
 -format mut be 2 Alphabetic characters followed by 3 decimals
 -names can be re-assinged
 -the same name cannot be used twice

data structure:
 -Robot (class)
    - used names (class varibale): collection of previously used robot names
    - name (instance variable) : robot initialised with a new random name
    - reset (method): resets the robot name

algorithm:
- name generator:
    -chose 2 random alphabetic characters and 3 random intengers
    -check whether name is availble
    -if so assing name

"""
import random

class Robot:
    
    used_names = []

    def __init__(self):
        self._name = self._name_generator()
    
    @property
    def name(self):
        return self._name

    def reset(self):
        self._name = self._name_generator()

    @classmethod
    def _name_generator(cls):

        while True:

            character_1 = chr(random.randint(65, 90))
            character_2 = chr(random.randint(65, 90))
            digit_1 = random.randint(0, 9)
            digit_2 = random.randint(0, 9)
            digit_3 = random.randint(0, 9)

            name = character_1 + character_2 + str(digit_1) + str(digit_2) + str(digit_3)

            if name not in cls.used_names:
                break

        cls.used_names.append(name)
        cls.name = name

        return name
    

    

    
    

        
