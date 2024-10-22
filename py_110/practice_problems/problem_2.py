"""
Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.


Problem:
    - Create a function that returns the minimum sum of 5 consecutive numbers in the list

Rules:
    - If the list contains fewer than 5 elements the list should return None

Examples:
    print(minimum_sum([1, 2, 3, 4]) is None)
    print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)

    - 1 + 2 + 3 + 4 + 5 = 15
    - 2 + 3 + 4 + 5 - 5 = 9

    print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)

    - 1 + 2 + 3 + 4 + 5 = 15
    - 2 + 3 + 4+ 5 + 6 = 20

    print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
    print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

Algorithm:
    - Check if list length < 5, if so return None
    - Use while loop to iterate trough list
        - Start from first index and get i, i+1, i+2, i+3, i+4 
        - if i+4 is in the list other wise break
        - move to next index
    - Sum values and add to output_list
    - return minimum value from output list

"""

def minimum_sum(number_list):

    output_list = []
    
    if len(number_list) < 5:
        return None
    
    index = 0

    while True:
        if index + 4 < len(number_list):
            sum_value = sum([number_list[index] + 
                            number_list[index + 1] +
                            number_list[index + 2] +
                            number_list[index + 3] +
                            number_list[index + 4]]
                            )
            output_list.append(sum_value)

            index += 1
        else:
            break
    
    return min(output_list)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)