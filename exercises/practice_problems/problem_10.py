"""

Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

Problem:
    Create a function that takes strings of digits as an argument and returns the number of even-numbered substrings

Rules:
    - Count each occurence of a substring

Examples:

    print(even_substrings('1432') == 6)

    '1'
    '14'#
    '143'
    '1432'#
    '4'#
    '43'
    '432'#
    '3'
    '32'#
    '2'#

    print(even_substrings('3145926') == 16)
    print(even_substrings('2718281') == 16)
    print(even_substrings('13579') == 0)
    print(even_substrings('143232') == 12)

Algorithm:
    - build substrings from string
        -cycle through characters in string
            -slice string at increasing end points from that character to end of string
            -append substring to output list
            -return output list
    - cycle through substrings and check whether they are even
    - if they are even append to list and return list

"""

def get_substrings(input_string):

    substrings = []

    for i in range(len(input_string)):
        for j in range(i+1,len(input_string)+1):
            substrings.append(input_string[i:j])
        
    return substrings



def even_substrings(input_string):
    substrings = get_substrings(input_string)

    return len([string for string in substrings if int(string) % 2 == 0])


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)