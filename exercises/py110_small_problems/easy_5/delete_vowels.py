"""
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

Program
Input: String
Out



"""

def remove_vowels(input_string_list):

    output_list = []

    for input_string in input_string_list:
        output_list.append(''.join([character for character in input_string if character not in 'aeiouAEIOU']))

    return output_list


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
