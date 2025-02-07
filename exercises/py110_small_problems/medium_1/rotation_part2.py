"""
Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

Input 1: number to rotate
Input 2: Index from end of digit to rotate

Algorithm:
# convert input number to string
# select index of digit to rotate and pop from string
# add digit back on to end of sting
# convert to integer and return rotated number

"""

def rotate_rightmost_digits(number, index):

    number_string = list(str(number))

    digit = number_string.pop(-1 * (index))

    number_string.append(digit)

    return int(''.join(number_string))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
