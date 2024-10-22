"""
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. 
If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k 
must be related to each other such that s == t * k. 

The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

Problem:
    Create a fucntion that takes a nonempty string and returns a tuple consisting of a string and an integer.

    s: String argument
    t: String component of tuple
    k: Integer componet of tuple

    s = t * k

Rules:
    - Strings are non-empty
    - string consists entirely of lowercase alphabetic letters
    - t is shorted possible substring
    - k is largest possible repeat

Examples:
    print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
    print(repeated_substring('xyxy') == ('xy', 2))
    print(repeated_substring('xyz') == ('xyz', 1))
    print(repeated_substring('aaaaaaaa') == ('a', 8))
    print(repeated_substring('superduper') == ('superduper', 1))

Algorithm:
    - create repeat_substring variable
    - cycle through characters in the string
        - append character to repeat_substring variable
        - check if repeat_substring is repeated segment:
            - for length of repeated_substring get next characters
            - if next characters are equal to the repeat_substring then it is repeated
        - if yes break loop
    - count number of occurences of repeated segment
    - return repeated segmnet and count
        

"""

def repeated_substring(input_string):
    substring = ''

    for idx,character in enumerate(input_string):
        substring += character

        next_segment = input_string[idx + 1: idx + 1 + len(substring)]

        if next_segment == substring:
            break
    
    return (substring,input_string.count(substring))
    




print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))