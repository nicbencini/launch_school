class Car:

    manufacturer = 'Ford'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    
    def show_manufacturer(self):
        print(f'{self.__class__.manufacturer=}')
        print(f'{self.manufacturer=}')

car_1 = Car('Toyota')
car_1.show_manufacturer()