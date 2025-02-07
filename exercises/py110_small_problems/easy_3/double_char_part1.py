"""
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

Algorithm:
- Cycle through characaters in the string and double 
"""

def repeater(input_string):
    return ''.join([f'{character}{character}' for character in input_string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

