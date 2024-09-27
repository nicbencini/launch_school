"""
Write a function that takes a string argument and returns a list of substrings of that string. 
Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

Problem:
Input: sting
Output: List of strings

Example:

a -> [0:1]
ab -> [0:2]
abc -> [0:3]

[0:i+1]

Algorithm:
- Cycle through characters in string
- For each character index slice string up to that point and append result to list
- Return list 

"""

def leading_substrings(input_string):
    return [input_string[0:i+1] for i in range(len(input_string))]


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
