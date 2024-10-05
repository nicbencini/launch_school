"""

Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).

Problem:
    - Create a function that counts the number of pairs in a list of integers

Rules:
    - Pair is two equal integers
    - pairs need to be seperated by number
    - Once a number is added to a pair it gets removed

Examples

    print(pairs([1, 2, 5, 6, 5, 2]) == 2)
    print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)

Algorithm:
    
    - Create variable to hold pair count
    - Create dictionary of available numbers
    - Cycle through list of numbers
        - For each number cycle through available numbers dictionary
            - If number is available and equal to current number then form pair
            - Mark current number and paired number as no longer being available in dictionary
    - Return pair count

Pseudo Code for Main Function:
    START
    
    # received list of integers called "number_list"

    SET available_numbers_dictionary = {KEY = index: VALUE = boolean to highlight availability}
    SET "pair_count" = 0

    FOR "number" in "number_list"
        # mark index of "number" and next number as not available in "available_numbers_dictionary"
        # cycle through available numbers, if "available_number" matches "number" increase "pair_count" by 1
        # mark "available_number" as no longer available
    
        
    return "pair_count"
    END

"""

def pairs(number_list):

    pair_count = 0

    available_numbers = {i:True for i in range(len(number_list))}

    for i,number in enumerate(number_list):

        available_numbers[i] = False
        if i+1 in available_numbers:
            available_numbers[i+1] = False

        for key,value in available_numbers.items():

            if value and (number_list[key] == number):
                pair_count += 1
                available_numbers[key] = False

    return pair_count

print(pairs([1, 2, 5, 6, 5, 2]) == 2)
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)