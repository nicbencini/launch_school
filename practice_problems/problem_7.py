"""
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. 
For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], 
the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

Problem:
    - craete a function that takes a list of integers as an argument and returns the number of identical pairs

Rules:
    - A pair is a set of identical numbers
    - If list is empty or contains one value return 0
    - count each complete pair once
    
Examples:
    print(pairs([3#, 1, 4, 5#, 9#, 2, 6, 5, 3#, 5#, 8, 9#, 7]) == 3)

    print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
    print(pairs([]) == 0)
    print(pairs([23]) == 0)
    print(pairs([997, 997]) == 1)
    print(pairs([32, 32, 32]) == 1)
    print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

Data:
    - Input: List of numbers
    - output: Integer representing number of pairs

Algorithm:
    - craete variable for pair count
    - create remaining_numbers dictionary
    - cycle through numbers in input list
        - flag number as not being remaing in dictionary
        - check dictionary for a second number that matches
        - if a second number matches then flag it as not remaining and add 1 to pair_counter
    -return pair_counter
"""

def pairs(numbers_list):
    pair_count = 0
    remaining_numbers = {index:True for index in range(len(numbers_list))}

    if len(numbers_list) <= 1:
        return 0
    
    for index,number in enumerate(numbers_list):
        output_list = []
        
        if remaining_numbers[index] == True:

            remaining_numbers[index] = False

            for key,value in remaining_numbers.items():
                
                if value and numbers_list[key] == number:
                    print(f'{numbers_list[key]} is {number}')
                    pair_count += 1
                    remaining_numbers[key] = False
                


    print(pair_count)

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)