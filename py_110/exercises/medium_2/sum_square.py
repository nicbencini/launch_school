"""

Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.

Problem:

Write a function that computes the difference between:
the square of the sum 
of the first count positive integers

and 

the sum of the squares of the first count positive integers.


Rules:
# Intgers are positive
# Count positive integers include the integer porvided
# 

Examples:
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
# 2640 
print(sum_square_difference(1) == 0)           # True
# 0 --> (1)**2 - (1**2)

print(sum_square_difference(100) == 25164150)  # True

Data:

Input: Integer
Output: Result

Algorithm:
# Create range up to and including integer porvided
# first result is the sum range and square it
# second result is obtianed by cycling through the integers in the list and squaring them individually and summing the result
# return the subtracted value

"""

def sum_square_difference(input_number):

    number_range = range(1,input_number + 1)

    square_of_sum = (sum(number_range))**2

    sum_of_squares = sum([number**2 for number in number_range])

    return square_of_sum - sum_of_squares



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True