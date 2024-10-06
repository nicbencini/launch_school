"""
Create a function that takes two strings as arguments and returns True if some portion of the characters in the first 
string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

Problem:
    Create a function that takes two strings as arguments and returns True if some portions of the characters in the first string can be rearrange to match the characters in the second.

Rules:
    - strings contain only lowercase alphabetic characters
    - neither string will be empty

Examples:
    print(unscramble('ansucchlohlo', 'launchschool') == True)
    print(unscramble('phyarunstole', 'pythonrules') == True)
    print(unscramble('phyarunstola', 'pythonrules') == False)
    print(unscramble('boldface', 'coal') == True)

Algorithm:
- cycle through characters in second string
    - check if the characters are present in the first string
    - if a character is not present break and return false
    - otherwise return true
"""

def unscramble(string_1, string_2):

    for character in string_2:
        if character not in string_1:
            return False
    
    return True


print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)