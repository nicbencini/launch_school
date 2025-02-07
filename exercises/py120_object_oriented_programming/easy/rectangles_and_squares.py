"""
Write a class called Square that inherits from the Rectangle class. The Square class is used like this:
"""

class Rectangle:

    def __init__ (self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @ width.setter
    def width(self, new_width):

        if not isinstance(new_width,int):
            raise ValueError('Width must be integer')
        
        self._width = new_width
    
    @property
    def height(self):
        return self._height
    
    @ height.setter
    def height(self, new_height):

        if not isinstance(new_height,int):
            raise ValueError('Height must be integer')
        
        self._height = new_height

    @property
    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width,width)


square = Square(5)
print(square.area == 25)      # True