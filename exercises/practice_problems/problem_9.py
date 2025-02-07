"""

Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. 
Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.


Problem:
    Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string

Rules:
    - overlapping strings don't count
    - second argument is never empty
    - second string may not exist if first

Examples:
    print(count_substrings('babab', 'bab') == 1)
    print(count_substrings('babab', 'ba') == 2)
    print(count_substrings('babab', 'b') == 3)
    print(count_substrings('babab', 'x') == 0)
    print(count_substrings('babab', 'x') == 0)
    print(count_substrings('', 'x') == 0)
    print(count_substrings('bbbaabbbbaab', 'baab') == 2)
    print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
    print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

    
Algorithm:
    - replace substirng in string with ' '
    - count spaces

"""

def count_substrings(string_1, string2):

    if string2 in string_1:
        return string_1.replace(string2, ' ').count(' ')

    return 0

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)