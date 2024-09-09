"""
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. 
In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation 
of that integer.

You may not use any of the standard conversion functions available in Python, such as str. 
Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

Problem

Input: integer
Output: string reperesentation of integer


Examples:

12345 = 

12345 % 10 = 5
12345 % 100 = 45
12345 % 1000 = 345
12345 % 10000 = 2345
12345 % 100000 = 12345

12345 /10 1234.5
12345 /100 = 123.45
12345 /1000 = 12.345
12345 / 10000 = 1.2345
12345 / 100000 = 0.12345

(12345 % 10**1) / 10**0 = 5
((12345 % 10**2) - (12345 % 10**1))/ 10**1 = 4.5

Formula:
((value % 10**i) - value % 10**i-1)/10**i-1

Algorithm

- Create while loop and divide number by 10 progressively until result is less than 1
- Whithin while loop apply formula for getting each integer of number
- Use dictionary to get string value for int using value as key
- return string


Code

"""

def integer_to_string(input_integer):

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


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True


