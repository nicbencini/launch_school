"""
Write a function that takes a string of digits and returns the appropriate number as an integer. 
You may not use any of the standard conversion functions available in Python, such as int. 
Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; 
assume all characters are numeric.

Problem

Inputs: string of digits
Output: integer

Implicit Rules:
- Do not use standard conversion functions
- Use characters in string
- Do not worry about sign or invalid characters

Examples:

1234 = 1000 + 200 + 30 + 4

Algorithm

- Creat global integer variable and assign it to zero
- Cycle through each character in the string in reverse
- Use match case to check which integer the chatacter matches
- Get position of integer based on its index.
- Depending on position of integer in string multiply that number by the order and add it to the global output integer
        0 = 1 = 10**0
        1 = 10 = 10**1
        2 = 100 = 10**2
        .....
- return global integer        

Code
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


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

