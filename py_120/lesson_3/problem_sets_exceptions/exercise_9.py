numbers = [1, 2, 3, 4, 5]

def lbyl(input_list):

    if len(input_list) >= 6:
        return input_list[5]
    
    return None

def afnp(input_list):

    try:
        return input_list[5]
    except IndexError:
        return None

print(lbyl(numbers))
print(afnp(numbers))

str1 = "I'm a string"
str2 = str1

class Point:
    def __init__(self, x, y):
        self.coordinates = {'x': x, 'y': y}

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        return self.coordinates == other.coordinates

point1 = Point(5, 10)
point2 = Point(5, 10)
point3 = point1
point1.coordinates['x'] = 4

print(point1 == point2)
print(point2 == point3)
print(point1 == point3)
print(point3 is point1)