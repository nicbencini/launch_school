class Recatangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    

rect_1 = Recatangle(4,3)

print(rect_1.width)
print(rect_1.height)

rect_1.height = 5


