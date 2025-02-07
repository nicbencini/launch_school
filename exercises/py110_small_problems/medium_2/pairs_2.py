"""
Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).

Program:
    Write a function that takes a list of inegers as input and counts the number of pairs.

Rules:
    - A pair is defined as two equal integers seperated by some other integers
    - Once an number forms a pair it cannot form another
    - numbers are all positive

Examples:
    print(pairs([1, 2, 5, 6, 5, 2]) == 2)
    print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)

    [1,2,6,8]

Data:
    Input: list of integers
    Output: single integer

Algorithm:
    - create a dictionary of pairs (key is the number: list of indices where it occurs)
    - cycle through numbers in list and add index to dictionary based on key
    - for each key if length of indices < 2 then it does not form a pair
    - otherwise if it is larger than 2:
        - check for consecutive indices
        -cycle through indeces (while loop):
            if next index is consecutive then ignore and grab next available index
            -if index is found remove from list and repeat

"""

def check_for_pairs(indices_list):

    indices_list = indices_list.copy()

    pair_count = 0
    
    while len(indices_list) >= 2:

        
        
        if indices_list[0] + 1 == indices_list[1] and len(indices_list) >= 3:
            indices_list.pop(0)
            indices_list.pop(1)
        else:
            indices_list.pop(0)
            indices_list.pop(0)

        pair_count += 1
    
    return pair_count

        



def pairs(integer_list):

    pair_count = 0

    pair_dictionary = {}

    for idx,number in enumerate(integer_list):

        if number not in pair_dictionary:
            pair_dictionary[number] = []
    
        pair_dictionary[number].append(idx)

    pair_items = pair_dictionary.items()
    
    for idx,item in enumerate(pair_items ):

        if len(item[1]) > 1:

            pairs = check_for_pairs(item[1])

            pair_count += pairs
    
    return pair_count



        
    


print(pairs([1, 2, 5, 6, 5, 2]) == 2)
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)