"""

A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, 
but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

Problem: 
Create a function that returns the next featured number.

Rules:
# a featured number is odd
# a feateured number is a multiple of 7
# a feature number has unique digits
# largest featured number is 9876543201
# all numbers are integers

Examples:
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

Data:
Input: Starting number
Output: Next featured number

Algorithm:
# Check whether number is larger than  9876543201 if so return error message
# Craete range from input number to 9876543201
# Cycle through the numbers in the range using a for loop
# Check whether number is a featured number
    # check if number is odd
    # check if number is a multiple of 7
    # check if number has unique digits using helper function
        # convert number to string
        # cycle to through characters in string
        # if the count of that character is larger than 1 then the number does not have unique digits
        # return False
# If the number is a featured number return that number

"""

def unique_digits(number_to_check):

    number_string = str(number_to_check)

    for char in number_string:
        if number_string.count(char) > 1:
            return False
    
    return True



def is_featured_number(number_):
    
    if number_ % 2 != 0 and number_ % 7 == 0 and unique_digits(number_):
        return True
    
    return False

def next_featured(number):


    error_message = ("There is no possible number that "
         "fulfills those requirements.")
    
    max_featured_number = 9876543201

    if number >= 9876543201:
        return error_message
    
    for i in range(number + 1, max_featured_number + 1):

        if is_featured_number(i):
            return i



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True