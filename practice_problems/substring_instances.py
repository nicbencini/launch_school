"""

Write a function that takes two strings as input, `full_text` and `search_text`,
and returns the number of times `search_text` appears in `full_text`.

Problem:
    Create a function that takes two strings as an input and returns the number of tiemse the second string appears in the first.

Rules:
    - all input strings are lowercase
    - only contains alphabetic characters


Examples:
    solution('abcdeb','b') # should return 2 since 'b' shows up twice
    solution('aaabbbcccc', 'bbb') # should return 1

Data:
    Input 1: String to search in
    Input 2: String to search for

    output: integer (count)

Algortithm:
    - use count method to count number of occurences of substirng in string

"""

def solution(full_text, search_text):
    return full_text.count(search_text)

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1
