"""
Write a function that takes a string as an argument and returns True 
if all parentheses in the string are properly balanced, False otherwise. 
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Note that balanced pairs must start with a (, not a ).

Problem
Input: String
Output: Bool

Rule:
- Matching parentese start with ( and end with ).
- Nested () should be considered
- No paraentheses should return True

Examples:

"What (is) this?" -> count 1 - 1 = 0
"What is) this?" -> count = -1 
"What (is this?" -> count = 1
"((What) (is this))?" -> count = 1 + 1 - 1 + 1 -1 -1 = 0
((What)) (is this))?" -> count = 1 + 1 - 1 - 1 + 1 - 1 - 1 = -1
")Hey!(" = 0 # THIS IS WRONG
"What ((is))) up(" = 1 + 1 - 1 - 1 -1 + 1 = 0 THIS IS WRONG

Algorithm:
- Create parenthesis counter. Counter cannot go below 0.
- Create open flag to check if paranthesis are still open
    - If '(' then add 1 to open_flag
    - If ')' then subtract 1 from open_flag 
    - If open flag goes below 0 then fail
    - If open_flag is not 0 when loop s complete then fail
- Cycle through characters in string
- If string does not contain '(' or ')' return True
- If character is '('  set flag to open
- If character is ')' remove one from count
"""

def is_balanced(input_string):

    counter = 0

    for character in input_string:
        if character == '(':
            counter += 1
        elif character == ')':
            counter -= 1
        
            if counter < 0:
                return False
            
        else:
            pass

    if counter != 0:
        return False
    else:
        return True


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True



