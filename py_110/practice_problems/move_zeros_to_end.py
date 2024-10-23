"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Problem:
    - Write an algorithm that takes an array and moves all the zeros to the end.

Rules:
    - Order of other elements is preserved
    - lists always contain values
    - lists always contain zeros

Examples:
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0])
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

Algorithm:
    - Use list comprehension to check if list item is equal to zero
        - if not zero add to first list
        - if it is zero add to second list
    return first list + second list


"""

def move_zeros(input_list):

    return [number for number in input_list if number != 0] + [number for number in input_list if number == 0]

print(move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0])
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])