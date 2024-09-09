"""
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

Program
Input: Positive Integer
Output: List of digits

Algorithm
- convert integer into string
- return characters of string as list

"""

def digit_list(input_integer):
    return [int(number) for number in str(input_integer)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
