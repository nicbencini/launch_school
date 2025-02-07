"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). 
First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of 
their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. 
In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these 
letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the 
same length sorted in ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples 
and "Example Tests".

Hopefully other examples can make this clearer.



problem:
    To create a function that returns a string in which each lowercase latters in s1 or s2 appears as many times as its maximum if the maximum is greater than 1.

Rules:
    - maximum number of lowercase letters must be greater than one
    - the substrings will be prefixed by the number of the string they appear in
    - if substings contain equal number of letter then they will be prefixed by =
    - substrings will be organised in decreasing ordre of length
        if length is equal then they will be sorted in ascending lexographical order (soreted by code point)
    - substirngs seperated by /
    - only lower case letters to be considered

Examples:
    s1 = "my&friend&Paul has heavy hats! &"
    s2 = "my friend John has many many friends &"
    mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

    s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
    s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
    mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

    s1="Are the kids at home? aaaaa fffff"
    s2="Yes they are here! aaaaa fffff"
    mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

    s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
    s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
    mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"

Data:
    Input_1 : first string
    Input_2 : second string
    output : resulting substring

Algorithm:
    - create substring dictionary
    - cycle through characters in first string
        - if character is lowercase:
            - get count of character:
                - if count > 1
                    - check if character is in string_2
                        -if not:
                            add to substring dictionary
                    - if yes:
                        - check if the count of character is higher in string 1 or 2 or equal:
                            - add substiring to dictionary with correct prefix 
    - repeat above for string b adding only lowercase characters not in string_1
    - created soreted list from dictionary based on length and lexography
    - concatenate to form string

"""

def rank(substring):

    length = len(substring)*-1
    number = substring.split(':')[0]
    alpha = substring.split(':')[1]

    return (length,number, alpha)


def mix(string_1, string_2):
    
    characters = {character for character in string_1 + string_2 if character.islower()}

    substring_list = []

    for character in characters:

        count_1 = string_1.count(character)
        count_2 = string_2.count(character)

        if count_1 > 1 and count_1 == count_2:
            substring_list.append(f'=:{character*count_1}')
        elif count_1 > 1 and count_1 > count_2:
            substring_list.append(f'1:{character*count_1}')
        elif count_2 > 1 and count_2 > count_1:
            substring_list.append(f'2:{character*count_2}')
        else:
            pass

        
    substring_list.sort(key=rank)

    return '/'.join(substring_list)

print(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp")== '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
print(mix("looping is fun but dangerous", "less dangerous than coding") == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
print(mix(" In many languages", " there's a pair of functions") == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
print(mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo")
print(mix("codewars", "codewars") == "")
print(mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
