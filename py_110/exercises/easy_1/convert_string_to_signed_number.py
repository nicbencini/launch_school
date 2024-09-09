"""
In the previous exercise, you developed a function that converts simple numeric strings to integers. 
In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. 
The string may have a leading + or - sign; if the first character is a +, your function should 
return a positive number; if it is a -, your function should return a negative number. If there is no sign, 
return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. You may, however, 
use the string_to_integer function from the previous exercise.


Problem

Input: string

Output: signed integer

Algorithm

- Check whether input string starts with + or - and remove them so that string_to_interger function can run
- Check if input string starts with -
- If it starts with - then multiply output by -1
- return resultant value


Code:
"""
def string_to_integer(input_string):

    integer_dictionary = {'0': 0,
                          '1': 1,
                          '2': 2,
                          '3': 3,
                          '4': 4,
                          '5': 5,
                          '6': 6,
                          '7': 7,
                          '8': 8,
                          '9': 9}
    
    output_integer = sum([integer_dictionary[number]*(10**i) for i,number in enumerate(reversed(input_string))])

    return output_integer

def string_to_signed_integer(input_string):
    
    if input_string.startswith('+'):
        return string_to_integer(input_string[1::])
    elif input_string.startswith('-'):
        
        return string_to_integer(input_string[1::]) * -1
    else:
        return string_to_integer(input_string)



print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True


