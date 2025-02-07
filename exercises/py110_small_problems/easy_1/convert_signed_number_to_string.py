"""
In the previous exercise, you developed a function that converts non-negative numbers to strings. 
In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. 
You may, however, use integer_to_string from the previous exercise.

Problem

Input: signed integer
Output: string

Implicit rules: 
- If interger is below 0 then add '-' to string otherwise add '+'
- Standard conversion functions cannot be used

Algorithm:
- Run integer_to_string function
- Check whether integer is below zero
- If it is add '-' to front of string 
- Otherwise add '+' to front of string

Code:
"""

def integer_to_string(input_integer):

    input_integer = abs(input_integer)

    integer_dictionary = {0: '0',
                          1: '1',
                          2: '2',
                          3: '3',
                          4: '4',
                          5: '5',
                          6: '6',
                          7: '7',
                          8: '8',
                          9: '9'
                          }

    output_string =''

    count = 1

    while True:

        value = int(((input_integer % 10**count) - (input_integer % 10**(count-1)))/10**(count -1))
        value_string = integer_dictionary[value]

        output_string += value_string
        
        if  input_integer/(10**(count)) < 1:
            break

        count += 1

    return output_string[::-1]

def signed_integer_to_string(input_integer):

    if input_integer < 0:
        return f'-{integer_to_string(input_integer)}'
    elif input_integer > 0:
        return f'+{integer_to_string(input_integer)}'
    else:
        return '0'
    

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True


