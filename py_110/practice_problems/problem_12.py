"""
Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence 
"Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

Problem:
    Create a function that takes a string as an argument and returns True if the string is a pangram.

Rules:
    -pangrams are sentences that contain every letter of the alphabet at least once
    -case is irrelevant
    -punctuation is present

Examples:
    print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
    print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
    print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
    print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
    print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

Algorithm:
    - convert string to lowercase
    - create list with all letters in the alphabet
    - cycle through list and check whether it is present in the sentence
        - if a letter is not present in the sentence break and return False
        - otherwise return True

"""

def is_pangram(input_string):
    input_string = input_string.lower()

    alphabet = 'qwertyuiopasdfghjklzxcvbnm'

    for letter in alphabet:

        if letter not in input_string:
            return False
        
    return True


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)