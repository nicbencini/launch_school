"""

A merge sort is a recursive sorting algorithm that works by breaking down a list's elements into nested sub-lists, then combining those nested sub-lists back together in sorted order. 
It is best explained with an example. Given the list [9, 5, 7, 1, 8, 2, 0, 6], let's walk through the process of sorting it with merge sort. 
We'll start off by breaking the list down into nested sub-lists:

Copy Code
[9, 2, 7, 6, 8, 5, 0, 1] -->              # initial list
[[9, 2, 7, 6], [8, 5, 0, 1]] -->          # divide into two lists
[[[9, 2], [7, 6]], [[8, 5], [0, 1]]] -->  # divide each sub-list in two
# repeat until each sub-list contains only 1 value
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]]
In the first step, we partition the list into a list of two sub-lists, so that each sub-list contains approximately half of the entries. In the next step, 
we partition each sub-list in the same way. This process repeats until each of the innermost lists contains exactly one element.

We now work our way back to a flat list by merging each pair of nested sub-lists in the proper ascending order:

Copy Code
[[[[9], [2]], [[7], [6]]], [[[8], [5]], [[0], [1]]]] -->
[[[2, 9], [6, 7]], [[5, 8], [0, 1]]] -->
[[2, 6, 7, 9], [0, 1, 5, 8]] -->
[0, 1, 2, 5, 6, 7, 8, 9]
For example, on the 2nd line, we merge [2, 9] with [6, 7], which becomes `[2, 6, 7, 9].

Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. 
The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will have the same data type: 
either all numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.


Problem:
    - Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order using a merge sort algorithm.

Rule:
    - Algorithm should split list recursively into sublist of single items
    - Lists can contain numbers and text
    - Lists always contain values

Examples:
    print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
    print(merge_sort([5, 3]) == [3, 5])
    print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
    print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

Algorithm:
    - Partition list into sublists of single values
    - cycle through sublists in pairs and merge the values using merge algorithm
        - use while loop 
        - merge and sort list and then redefine partion list after each cycle
        - break while loop when parition list only contains one item
    - cycle through until all lists are merged
    - return sorted list

"""


def swap_items(input_list):

    swap_result = False

    for idx, item in enumerate(input_list):

        if idx + 1 < len(input_list):
            next_item = input_list[idx + 1]
            
            if item > next_item:
                input_list[idx], input_list[idx + 1] = input_list[idx + 1], input_list[idx]
                swap_result = True
    
    return swap_result


def merge(list_1, list_2):

    combined_list = list_1 + list_2

    while True:

        if not swap_items(combined_list):
            break

    return combined_list

def merge_sort(input_list):

    partitioned_list = [[item] for item in input_list]

    while True:

        if len(partitioned_list) == 1:
            break
        
        new_partitioned_list = []

        for idx in range(0,len(partitioned_list),2):

            if idx + 1 < len(partitioned_list):

                sublist = partitioned_list[idx]

                next_sublist = partitioned_list[idx+1]

                merged_list = merge(sublist, next_sublist)

                new_partitioned_list.append(merged_list)
            
        if len(partitioned_list) % 2 != 0:
            new_partitioned_list.append(partitioned_list[-1])

        
        partitioned_list = new_partitioned_list

    return partitioned_list[0]



# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)