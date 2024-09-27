"""
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.


Program
Input: Sequnce of integers
Output: Fileted sequenc of integers

Rules:
- Order of integers to be maintained

Algorithm:
- Cycle through intergers in sequence and add to local list 
- If value already in local list do not add it
- Return local list


"""


def unique_sequence(input_sequence):
    
    output_list = []

    for number in input_sequence:
        if number not in output_list:
            output_list.append(number)

    return output_list




original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
