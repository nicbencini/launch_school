"""
Write a function that rotates a list by moving the first element to the end of the list. 
Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.


Problem
Input: List
Output: Rotated List

Rules:
# Original list should not be modified
# Function returns a new list
# Return empty list if input is empty
# If input is not a list return None
# 

Algorithm:
# create empty list for output
# check if list length is larger than 1 item otherwise return original lists
# use list slicing to get 2nd element of list onwards and assign to output list
# append first element of list to output list
# return output list

"""

def rotate_list(input_list):

    if type(input_list) != list:
        return None
    
    elif len(input_list) < 2:
        return input_list

    rotated_list = input_list[1::]
    rotated_list.append(input_list[0])

    return rotated_list

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
