"""
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. 
Examine the examples to see what we mean. You may assume that the list always contains at least one number.

Program:
Input: list of numbers
Ouput: number

Algorithm:
- Create counter
- Cylce through numbers, and for each number add value to counter and append value of counter to output list
- Sum output list and return value 
"""

def sum_of_sums(numbers_list):

    counter = 0

    output_list = []

    for number in numbers_list:
        counter += number

        output_list.append(counter)
    
    return sum(output_list)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True
