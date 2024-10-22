"""
Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

Problem:
    - Create a function that takes a list of numbers. All of which are the same except one.
    - Find and return the number in the list that differes from all the rest

Rules:
    - The list will always contain at least 3 numbers
    - There will always be exactly one number that is different
    - Numbers can be floats

Examples:
    print(what_is_different([0, 1, 0]) == 1)
    print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
    print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
    print(what_is_different([3, 4, 4, 4]) == 3)
    print(what_is_different([4, 4, 4, 3]) == 3)

Algorithm:
    - Cycle through numbers in the list
    - Get count for number of times that number appears in the list
    - If that count is equal to 1 then return that number


"""

def what_is_different(number_list):
    for number in number_list:
        if number_list.count(number) == 1:
            return number
    
    return None


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)