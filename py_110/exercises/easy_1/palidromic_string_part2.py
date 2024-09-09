"""
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. 
If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

Problem:
Input: String 
Output: Boolean

Implicit Rules:
- Function should be case sensitive
- Fucntion should ignore all non-alphanumeric characters

Explicit Rules:

Algorithm:

Code:

"""


def is_real_palindrome(input_string):

    cleaned_string  = ''.join([character.lower() for character in input_string if character.isalnum()])

    return cleaned_string[::-1] == cleaned_string

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

