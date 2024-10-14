"""
Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.

Probelm:
    To create a fucntion that takes a string and counts the occurrences of each lowecase letter in the string.

Rules:
    - Return the count in a dictionary where the letters are keys ant thier counts are values.
    - All characters are lowercase

Examples: 
    -{'a': 1, 'c': 2, 'h': 2, 'l': 2, 'o': 2, 'u': 1 }

Data:
    - Input: String
    - Output: Dictionary

Algorithm:
    -Create an output dictionary (key is the letter, the value is the count)
    -Cycle through each letter in the string
        -Check if character is in the dictionary. If not add it
        -If the character is in the dictionary increase count by 1
    return the dictionary


"""

def letter_count(input_string):

    output_dictionary = {}

    for character in input_string:
        if character not in output_dictionary:
            output_dictionary[character] = 0
        
        output_dictionary[character] += 1

    print(output_dictionary)
    
    return output_dictionary

result = {'a': 1, 'c': 2, 'h': 2, 'l': 2, 'o': 2, 'u': 1 }

print(letter_count('launchschool')  == result)