"""
Write a function that takes a list as an argument and returns a list that contains two elements, 
both of which are lists. Put the first half of the original list elements in the first element of 
the return value and put the second half in the second element. If the original list contains an odd number 
of elements, place the middle element in the first half list.

Program:
Input: List
Output: List of first half of elements, list of second half of elements

Rules:
- If odd middle element gets added to first list

Algorithm:
- Get length of input list.
- Check whether it is odd or even
- Divide lenth in 2 to get index of middle. If odd allow for middle element.
- Split list using indexing
"""

def halvsies(input_list):
    list_length = len(input_list)

    if list_length % 2 == 0:
        middle = int(list_length/2)

    else:
        middle = int(list_length/2) + 1

    return [input_list[:middle], input_list[middle:]]
# All of these examples should print True

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

