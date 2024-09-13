"""
Given a list of strings, return a new list where the 
strings are sorted based on the highest number of 
adjacent consonants a string contains. If two strings 
contain the same highest number of adjacent consonants,
 they should retain their original order in relation 
 to each other. Consonants are considered adjacent if 
 they are next to each other in the same word or if 
 there is a space between two consonants in adjacent 
 words.

Problem:

Inputs: List of strings
Outputs: List of sorted strings

Explicit Rules:
-Strings sorted by highest number of adjacent consonants.
-If 2 strings contain the same number of adjacent
consonants they should retian thier original order in 
relation to each other
-Consonants are considered adjacent if they are next to
each other in the same word or if there is a space between
two consonats in adjacent words.

Implicit Rules:
-Input list strings may contain multiple words
-Is word consisting of vowels only put at the end of the list?

Data Structures:
- List 
- Dictionary

Algorithm:
# Create output word list
# Cylce through each word in the list
# Remove spaces from the words in the list
# Check if word consists of vowels only, if so return full length of word
 - cycle through characters in word 
 - check if character is vowel and add to count
 - if count is equal to length of word then word is all vowels
# Create list of vowels and cycle through characters 
in the list
    - for character in word if character is consonant increase counter
    - if character is vowel set counter back to 0
# Create dictionary with max consonant count per word as keys
# Sort dictionary by keys
# Return values from dictionary as output word list  
"""

def is_all_vowels(word):
    
    vowels = 'aeouiAEOUI'
    count = 0

    for character in word:
        if character in vowels:
            count += 1
    
    if count == len(word) and count != 0:
        return True
    
    return False


def sort_by_consonant_count(string_list):

    consonant_count_dictionary = {}
    vowels = 'aeouiAEOUI'
    output = []

    for string in string_list:
        word = string.replace(' ','')

        if is_all_vowels(string):
            consonant_count = len(string) -1

        else:
            for character in word:
                if character in vowels:
                    word = word.replace(character,'_')
            
            consonant_count = max(len(item) for item in word.split('_'))

        if consonant_count not in consonant_count_dictionary.keys():
            consonant_count_dictionary[consonant_count] = []
        
        consonant_count_dictionary[consonant_count].append(string)

    [output.extend(consonant_count_dictionary[key]) for key in sorted(consonant_count_dictionary,reverse=True)]
    
    return output

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']