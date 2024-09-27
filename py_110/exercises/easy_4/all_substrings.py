"""
Write a function that returns a list of all substrings of a string. 
Order the returned list by where in the string the substring begins. 
This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. 
Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:


Problem
Input: string
Output: List of strings

Algorithm:
- cycle through characters in string
- for each character build string with the previous character removed
- Run leading_substring on the new string and append the result to output list
- Return output list

"""

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

def leading_substrings(input_string):
    return [input_string[0:i+1] for i in range(len(input_string))]


def substrings(input_string):
    
    output_list = []

    for i in range(len(input_string)):
        new_string = input_string[i::]
        output_list.extend(leading_substrings(new_string))
    
    return output_list

print(substrings('abcde') == expected_result)  # True
