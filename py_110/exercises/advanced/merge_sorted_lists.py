"""

Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. 
You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

Problem:
    - Write a function that takes two soreted lists and returns a new list that contains all elements from both input lists in ascending sorted order.

Rules:
    - Do not use sorted function or method
    - Do not mutate the lists
    - Inputs may be empty lists
    - Duplicate numbers may occur

Examples:
    - print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
    - print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
    - print(merge([], [1, 4, 5]) == [1, 4, 5])
    - print(merge([1, 4, 5], []) == [1, 4, 5])

Algortihtm:
    - combine both lists
    - cycle through each item in the list. If it is smaller than the next item then swap them round
        - if a < b: list[a],list[b] == list[b],list[a]
        - 
    - repeat this until no furhter swaps occur
        - use flag to check whether swap has occured
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

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)