"""
Write a function that takes two list arguments, each containing a list of numbers, 
and returns a new list that contains the product of each pair of numbers from the arguments 
that have the same index. You may assume that the arguments contain the same number of elements.

Program
Input: 2 lists of numbers
Output: List of results of the multiplication

Algorithm:
- Cycle through each element in list
- Multiply element from one list with the element from the second list
- Add to global list and retur the result

"""

def multiply_list(input_list1, input_list2):

    output_list = []

    for i in range(len(input_list1)):
        output_list.append(input_list1[i] * input_list2[i])
    
    return output_list



list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
