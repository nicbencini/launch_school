"""
Write a function that combines two lists passed as arguments and returns a new list that contains all 
elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

Program
Input: 2 lists
Output: Combined list

Algorithm:
- cycle through both list
- append item from lists to a new list in sequence

"""

def interleave(input_list1, input_list2):

    output_list = []
    for i in range(len(list1)):
        output_list.append(list1[i])
        output_list.append(list2[i])
    
    return output_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
