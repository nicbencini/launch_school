class Mamal:

    def __init__(self):
        self.legs = 4

class Human(Mamal):

    def __init__(self):
        self.legs = 2

human_1 = Human()
print(human_1.legs)