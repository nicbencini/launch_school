"""

A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. 
If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's 
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.

Problem:
A function that takes 3 angles as arguments and returns the clasification of the triangle

Rules:
# If an angle is zero, the triangle is 'invalid'
# If the sum of the angles is not equal to 180, the triangle is 'invalid'
# if one angle is 90 degress, the triangle is 'right'
# If all angles are less than 90 degrees, the triangle is 'acute'
# If one angle is greater than 90 degrees, the triangle is 'obtuse'

Examples
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

Data:
Input_1: angle 1
Input_2: angle 2
Input_3: angle 3

Output: string representing the triangle type

Algorithm:
# Check if triangle is valid:
    # If one angle is equal to 0 it is invalid
    # If all angles dont add up to 180 it is invalid.
# If one angle is equal to 90, it is right
# If all angels are less than 90 it is acute
# If one angle is larger than 90, it is obtuse

"""

def invalid_triangle(angle_1_, angle_2_, angle_3_):

    if angle_1_ == 0 or angle_2_ == 0 or angle_3_ == 0:
        return True
    elif sum([angle_1_, angle_2_, angle_3_]) != 180:
        return True
    
    return False


def triangle(angle_1, angle_2, angle_3):

    if invalid_triangle(angle_1, angle_2, angle_3):
        return "invalid"
    
    elif angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        return "right"
    
    elif angle_1 < 90 and angle_2 < 90 and angle_3 < 90:
        return "acute"
    
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        return "obtuse"

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True