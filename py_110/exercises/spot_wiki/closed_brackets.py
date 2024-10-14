"""
The function is given a string consisting of a collection of three characters:

"(" open bracket
")" closed bracket
"J" Joker, which can be replaced by "(", ")" or ""

Develop a solution to determine if the given string represents a proper sequence of parenthesis; return True / False. 
Each open bracket on the left should have a corresponding closed bracket on the right. For example "(()())" is a proper sequence, 
"()(()" is not a proper sequence. The presence of Jokers adds an extra level of difficulty to the analysis because each "J" makes 
three possibilities to consider. An empty string is considered a valid string because it does not contain unbalanced brackets.

Problem:
    Develop a solution to determine if the given string represents a proper sequence of parenthesis

Rules:
    - The input string consists of '(' , ')' or 'J'
    - 'J' can be replaced by '(' , ')' or ''
    - Each open bracket on the left should have a corresponding closed bracket on the right
    - Empty string is valid because it does not contain unbalanced brackets

Examples:
    - closed_brackets("(J))") ➞ True
    - print(closed_brackets("(") == False)

Data:
    Input: String
    Output: Boolean

Algorithm:
    - if string is empty return True
    - create open_brackets variable
    - cycle through characters in string
        - if '(' add 1 to open brackets variable
        - if ')' subtract 1 from open brackets variable
        - if open_brackets variable goes below 0:
            break and return false
    - if 'J' and open_brackets != 0:
        - replace'J' with '(' and run brakcet check
        - replace'J' with ')' and run bracket check
    - if open_brackets variable == 0  return True


"""

def closed_brackets(input_string):

    bracket_count = 0
    j_count = 0

    for character in input_string:
        if character == '(':
            bracket_count += 1
        elif character == ')':
            bracket_count -= 1
        elif character == 'J':
            j_count += 1
        
        if bracket_count < 0:
            if j_count > 0:
                bracket_count += 1
                j_count -= 1
            else:
                return False
    
    while bracket_count > 0 and j_count > 0:
            bracket_count -= 1
            j_count -= 1

    
    if bracket_count == 0:
        return True
    
    return False




print(closed_brackets("(J))") == True)
# J can be replaced with (

print(closed_brackets("(") == False)
# Unbalanced open bracket.

print(closed_brackets("") == True)
# Empty string is a valid sequence.

print(closed_brackets("()J(") == False)
# Not possible to balance the brackets.

print(closed_brackets("J") == True)
# J can be replaced with an empty string.

print(closed_brackets(")(") == False)
# Numbers of ( and ) are the same but they are in the wrong places.

print(closed_brackets("J)(J") == True)
# First 'J' can be replaced with '(' and second with ')'

print(closed_brackets("()") == True)
# A proper sequence of balanced brackets.