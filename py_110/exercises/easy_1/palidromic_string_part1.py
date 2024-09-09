"""
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. 
A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

Problem
Input: String
Output: Boolean

Explicit Rules:
- Case matters
- All characters matter

Implicit Rules:
- Paildrom is a word that reads same forwards and backwords.

Algorithm

- if reverse of word is equal to the word then it is a palidrome

Code
"""

def is_palindrome(input_string):

    return input_string[::-1] == input_string 


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)


