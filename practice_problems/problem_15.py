"""
Create a function that takes a string argument that consists entirely of numeric digits 
and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

Problem:
    Create a function that takes a string argument that consists entirely of numeric digits and 
    computes the gretest product of four consecutive digits of the string

Rules:
    - The argument will always have more than 4 digits

Examples:
    print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
    print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
    print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
    print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

Data:
    Input: String
    Output: Integer

Algorithm:
    - get all possible substrings of 4 characters from the input string
        -cycle through characters in the string
        - slice from that index up to the next 4 indeces
        - if word is longer than 4 characters then convert to int and append to output list
    - cycle through the substrings and calculate the product
    - return the greatest product

"""

def get_substring_integers(number_string):

    output_integers = []

    for idx,character in enumerate(number_string):
        substring = number_string[idx: idx + 4]

        if len(substring) >= 4:
            output_integers.append(substring)
    
    return output_integers


def greatest_product(input_string):
    
   
    product_values = []

    substrings = get_substring_integers(input_string)

    for string in substrings:
        result = 1
        for character in string:
            result *= int(character)
        
        product_values.append(result)
    
    return max(product_values)
        
    




print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6