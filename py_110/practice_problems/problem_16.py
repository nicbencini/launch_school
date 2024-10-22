"""
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

Problem:
    Create a function that returns the count of distinctive case-sensitve alphabetic characters and number digits that occur more than once.

Rules:
    - input string contains only alphanumeric characters
    - valid characters appear are characters that appear more than once
    - if there are no valid characters the function should return 0
    - case should be ignored
    

Examples:
    print(distinct_multiples('xyz') == 0)               # (none)
    print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
    print(distinct_multiples('xX yY p zZ r') == 3)          # x, y, z
    print(distinct_multiples('u n u n u n ium') == 2)         # u, n
    print(distinct_multiples('multiplicity') == 3)      # l, t, i
    print(distinct_multiples('7657') == 1)              # 7
    print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
    print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5


Data:
    Input: string
    Ouptut: integer for count of duplicates

Algorithm:
    - create counter
    - cycle through characters in string
        - count number of time character appeares in sring
        - if it is greater than one increament counter by 1
    return counter

"""

def distinct_multiples(input_string):
    counter = 0

    input_string = input_string.lower()
    unique_characters = set(list(input_string))

    for character in unique_characters:
        if input_string.count(character) > 1:
            counter += 1
    
    return counter


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5