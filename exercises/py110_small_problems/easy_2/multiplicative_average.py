"""
Write a function that takes a list of positive integers as input, multiplies all of the integers together, 
divides the result by the number of entries in the list, and returns the result as a string with the value 
rounded to three decimal places.

Program
Input: List of integers
Output: Rounded integer result

Rules:
Result must be rounded to 3 decimal places.

Algorithm:
- Multiply all integers in list together
- Divide result by length of list
- Return result to 3 decimal places us round function
"""

def multiplicative_average(input_list):

    result = 1

    for number in input_list:
        result *= number

    return (str(round(result/len(input_list),3)))
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
