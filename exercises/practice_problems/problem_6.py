"""
Create a function that takes a string argument and returns a dict object in which the keys represent the 
lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

Problem:
    - create a function that takes a string and returns a dictionary of the lowercase letters

Rules:
    - Strings contain punctuation which shouldnt be counted
    - Stirngs can be empty in that case return empty dictionary
    - Strings can contain just punctuation

Examples:
    expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
    print(count_letters('woebegone') == expected)

    expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
                'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
    print(count_letters('lowercase/uppercase') == expected)

    expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
    print(count_letters('W. E. B. Du Bois') == expected)

    print(count_letters('x') == {'x': 1})
    print(count_letters('') == {})
    print(count_letters('!!!') == {})

Algorithm:
    - clean string to remove punctuation
    - cycle through characters in the string
        - if character is lowercase, add to dictionary and update count
    - return disctionary



"""

def count_letters(input_string):

    letter_dictionary = {}

    for character in input_string:
        if character.isalpha() and character.islower():
            if character in letter_dictionary:
                letter_dictionary[character] += 1
            else:
                letter_dictionary[character] = 1
    
    return letter_dictionary



expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})