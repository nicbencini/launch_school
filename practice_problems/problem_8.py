"""

Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. 
The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".


Problem:
    Create a function that returns the length of the the longest vowel substring

Rules:
    - Strings are non-empty
    - Strings consists of lowercase alphabetic characters
    - string can contain no vowels
    - stirngs do not contains spaces

Examles:
    print(longest_vowel_substring('cwm') == 0)
    print(longest_vowel_substring('many') == 1)
    print(longest_vowel_substring('launchschoolstudents') == 2)
    print(longest_vowel_substring('eau') == 3)
    print(longest_vowel_substring('beauteous') == 3)
    print(longest_vowel_substring('sequoia') == 4)
    print(longest_vowel_substring('miaoued') == 5)

Algorithm:
    - cycle through characters in string and replace consonants with spaces
    - split string into substrings using the spaces
    - get length of longest substring and return it


"""

def longest_vowel_substring(input_string):

    vowels = 'aeiou'

    foramtted_string = ''.join([char if char in vowels else ' ' for char in input_string])

    substrings = foramtted_string.split(' ')

    return max([len(substring) for substring in substrings])


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)