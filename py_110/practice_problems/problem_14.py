"""
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. 
If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

Problem:
    Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument.

Rules:
    - If a number is a multiple of both 7 and 11, count it just once
    - If the argument is negative return 0
    - Argument can be 0
    - Argument is not included as multiple

Examples:
    For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.
    print(seven_eleven(10) == 7)
    print(seven_eleven(11) == 7)
    print(seven_eleven(12) == 18)
    print(seven_eleven(25) == 75)
    print(seven_eleven(100) == 1153)
    print(seven_eleven(0) == 0)
    print(seven_eleven(-100) == 0)

Data:
    Input: integer
    Output: sum of multiples as integer

Algorithm:
    - create multiples list
    - check if number is greater than 0, if not return 0
    - create range from 1 to the number
    - cycle through numbers in the range:
        if number is multiple of 7 or 11 add to list
    - covert multiples list to set to remove duplicates and sum
    - return result

"""

def seven_eleven(input_number):
    multiples = []

    if input_number <= 0:
        return 0

    for number in range(1,input_number):
        if number % 7 == 0 or number % 11 == 0:
            multiples.append(number)
    
    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)