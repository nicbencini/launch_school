"""
Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list.

Problem
Input:List of numbers
Output:List of numbers

Algoritm:
- Create global count varaible
- Cycle through list and add number to count
- Append number to output list
- Return list

"""

def running_total(input_list):
    
    output_list = []

    count = 0

    for number in input_list:
        count += number
        output_list.append(count)

    return output_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

