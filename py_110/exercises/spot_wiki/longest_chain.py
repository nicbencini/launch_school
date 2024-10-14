"""
Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).

Problem:
    Write a function that takes a lowercase string as input and returns the length of the longest 
    substring that consists entirely of vowels.

Rules:
    - all characters are lowercase
    - strings consists of single words

Examples:
    - "roadwarriors" == 2
    - "suoidea" == 3

Algorithm:
    - cycle through characters in string and replace all consonants with a space
    - split the string using the space character 
    - get the length of the longest sub string

"""

def solve(input_string):
    
    vowels = 'aeiou'

    modified_string = ''.join([character if character in vowels else ' ' for character in input_string])

    substring_list = modified_string.split(' ')
    
    return max(len(string) for string in substring_list)


print(solve("roadwarriors") == 2)
print(solve("suoidea") == 3)