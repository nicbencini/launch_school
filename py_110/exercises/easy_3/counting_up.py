"""
Write a function that takes an integer argument and returns a list containing all 
integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

Program
Input = postive integer
Output = list of integers

Rules:
- argument always positive
- argument included in list
- output list in ascending order

Algorithm:
- Create range starting at 1 to argument + 1 
"""

def sequence(input_number):
    return list(range(1,input_number + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
