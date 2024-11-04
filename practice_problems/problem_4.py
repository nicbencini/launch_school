"""
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. 
If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Problem:
    - Create a function that takes a list of integers and returns a tuple with the closest pairs

Rules:
    - Pair is a tuple with integer closest in value
    - If there are multiple pairs that are equally close return the first occuring
    - numbers do not repeat

Examples:
    print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
    print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
    print(closest_numbers([12, 22, 7, 17]) == (12, 7))

Data:
Input: list of numbers
Output: tuple


Algorithm:
    - create output_tuple variable
    - create difference variable
    - cycle through numbers in the list
        -for each number cycle through other numbers and check which one is the closest
        -calculate the difference and if the difference is smaller is than the current difference update tuple
    return tuple
    
    -closest_number_helper(number, list):
        - create variable called difference
        - cycle through items in list and calculate difference to number if not equal to number
        - return number with min difference


"""

def closest(number, number_list):
    min_difference = 0
    output = None

    for num in number_list:
        if num != number:
            difference = abs(num-number)

            if min_difference == 0 or difference < min_difference:
                min_difference = difference
                output = num
    
    return output


def closest_numbers(lst):

    min_difference = None
    output_tuple = None
    
    for number in lst:
        closest_number = closest(number,lst)

        difference = abs(number - closest_number)

        if not min_difference or min_difference > difference:
            min_difference = difference
            output_tuple = (number,closest_number)

    return output_tuple


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))