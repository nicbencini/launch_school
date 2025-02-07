"""

A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, 
and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following 
four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.


Problem:
The goal is to craete a function that takes the length of 3 sides of a triangle and outputs the classification for the triangle.

Rules:
# Every side must be greater than 0
# The sum of the length of the two shortest sides must be greater than the longest side
# If all 3 sides are equal it is equilateral
# If only 2 sides are equal it is isosceles
# if all 3 sides are different it is scalene
# Inputs will be integers or floats

Examples:
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

Data:
Input_1: First side of the triangle
Input_2: Second side of the triangle
Input_3: Third side of the triangle

Output: String representing classification of the triangle

Algorithm:
# create parameters side_1, side_2 and side_3 for the 3 sides of the triangle
# check if any of the sides is equal to zero, if so return 'invalid'
# check if the sum of the two shortest sides is larger than the lenght of the longest side
    # pop the longest side from the list and sum the result. Check if result is larger than the longest side
    # if not return invalid
# check if side_1 == side_2 == side_3 if so return 'equaliateral'
# check if side_1 == side_2 != side_3 or side1 != side_2 == side_3 or side_1 == side_3 != side_2 if so return isosceles
# check if side_1 != side_2 != side_3 if so return scalene


"""

def check_sides(side_1, side_2, side_3):
    
    
    sides = [side_1, side_2, side_3]
    max_side = max(sides)

    sides.remove(max_side)
    
    if sum(sides) < max_side:
        return True
    
    return False

def check_equilateral(side_1, side_2, side_3):
    
    if side_1 == side_2 and side_2 == side_3 and side_3 == side_1:
        return True
    
    return False

def check_isosceles(side_1, side_2, side_3):
    
    if side_1 == side_2 and side_2 != side_3:
        return True
    elif side_2 == side_3 and side_3 != side_1:
        return True
    elif side_3 == side_1 and side_1 != side_2:
        return True

    return False 

def check_scalene(side_1, side_2, side_3):
    
    if side_1 != side_2 and side_2 != side_3 and side_3 != side_1:
        return True
    
    return False

def triangle(side_1, side_2, side_3):

    if side_1 == 0  or side_2 == 0  or side_3 == 0:
        return "invalid"
    
    elif check_sides(side_1, side_2, side_3):
        return "invalid"
    
    elif check_equilateral(side_1, side_2, side_3):
        return "equilateral"
    
    elif check_isosceles(side_1, side_2, side_3):
        return "isosceles"
    
    elif check_scalene(side_1, side_2, side_3):
        return "scalene"
    else:
        return "invalid"
    


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True