"""
Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. 
There will always be exactly one such integer in the input list.

Problem:
    create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times.

Rules:
    - There will always be exactly one such integer in the input list
    - Lists can only contain one item
    - lists can contain just a single item repeated
    - lists can contain negarive numbers

Examples:
    print(odd_fellow([4]) == 4)
    print(odd_fellow([7, 99, 7, 51, 99]) == 51)
    print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
    print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
    print(odd_fellow([0, 0, 0]) == 0)

Data:
    Input: list of integers
    Output: integer that appears odd number of times

Algorithm:
    - cycle through each number in list
    - count number of occurences of that number in the list
    - if the number of occurences is an odd number return that number

"""

def odd_fellow(number_list):

    for number in number_list:
        if number_list.count(number) % 2 != 0:
            return number
    
    return None


print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)