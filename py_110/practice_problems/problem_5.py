"""
Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, 
return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

Problem:
    - Create a function that takes a string and returns the character that occurs most frequently

Rules:
    - Upper case and lower case versions are the same
    - If there are multiple characters with the same frequency return the one that appears first

Examples:
    print(most_common_char('Hello World') == 'l')
    print(most_common_char('Mississippi') == 'i')
    print(most_common_char('Happy birthday!') == 'h')
    print(most_common_char('aaaaaAAAA') == 'a')

    my_str = 'Peter Piper picked a peck of pickled peppers.'
    print(most_common_char(my_str) == 'p')

    my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
    print(most_common_char(my_str) == 'e')

Data:
    Input: string
    Output: most common char

Algorithm:
    -create count variable
    -create character variable
    - clean sring by converting it to lowercase
    - cycle through characters in the string 
        - count each character within the string
        - if count of characters is greater than count variable value:
                - update count 
                - update character
    - return character

"""


def most_common_char(input_string):

    count = 0
    out_character = ''

    input_string = input_string.lower()

    for character in input_string:
        character_count = input_string.count(character)

        if character_count > count:
            count = character_count
            out_character = character

    return out_character



print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')