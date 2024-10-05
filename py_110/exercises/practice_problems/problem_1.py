"""
Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, 
and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

Problem:
- create a function that takes a list of number and determines home many unique numbers are smaller than it

Rules:
- When counting the numbers only count unique values
- List can contain only the same number
- Lists can contain single items

Examples:
    print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
    print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
    print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
    print(smaller_numbers_than_current([1]) == [0])

    my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
    result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
    print(smaller_numbers_than_current(my_list) == result)

Data:

    Input_1: list of numbers to count
    Output: list of counts for each number

Algorithm:
- Cycle through number in list
- For each number cycle through list of numbers
    - Create list to collect smaller numbers
    - If a number is smaller than the current number append to list
    - turn list to set to remove duplicates and get its lenth to find ammount of unique smaller numbers
    - append to output list

"""

def smaller_numbers_than_current(number_list):

    output_list = []

    for number in number_list:
        smaller_numbers = [value for value in number_list if value < number]

        number_of_smaller = len(set(smaller_numbers))

        output_list.append(number_of_smaller)
    
    return output_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)