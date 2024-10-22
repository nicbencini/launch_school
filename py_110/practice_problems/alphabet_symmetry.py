"""

Write a function that takes a list of words as input and returns a list of
integers. Each integer represents the count of letters in the word that occupy
their positions in the alphabet.

Problem:
    Write a function that takes a list of words and returns a list of integers that represents 
    the count of letters in the word that occupy thier positions in the alphabet.

Rules:
    - Case should not be considered
    - words only contain alphabetic characters
    - string are not empty

Examples:
    print(solve(["abode","ABc","xyzD"]) == [4, 3, 1])
    print(solve(["abide","ABc","xyz"]) == [4, 3, 0])

Algorithm:
    - create output list
    - cycle through words in the list
        - create a counter
        - change word to lowecase and cycle through each character
            -for each character get its index in the word
            -compare it against the index of the character in the alphabet string
            -if both are equal increase count by 1
    return output list


"""

def solve(string_list):

    count_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for string in string_list:
        letter_counter = 0

        string = string.lower()
        
        for character in string:

            if string.index(character) == alphabet.index(character):
                letter_counter +=1
        
        count_list.append(letter_counter)

    return count_list

print(solve(["abode","ABc","xyzD"]) == [4, 3, 1])
print(solve(["abide","ABc","xyz"]) == [4, 3, 0])