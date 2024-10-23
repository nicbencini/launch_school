"""

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

Problem:
    - given an nxn array, teturn the array elements arranged from outermost elements to the middle element, travelling clockwise.

Rules:
    - Matrices can be empty

Data:
    - Input: nxn matix
    - Output: sorted list

Algorithm:
    - check that matrix is not empty. if so return []
    - create output_list variable
    - while loop:
        - append first row of matrix to output_list and remove from matrix
        - append last column of matrix to output_list and remove from matrix
        - append last row of matrix to output_list and reomve from matrix
        - append first column of matrix to output_list and remove from matrix
        - break when there are no more columns and rows in matrix
    return output_list

Helper Functions:

    - remove_row(matrix, row_idx):
        - mutates original matrix
        - removes the sub_list (row) at row_idx
    
    - remove_column(matrix, col_idx):
        - mutates orignial matirx
        - cycles through sublists and removes the item at col_idx



"""

def remove_row(matrix, row_idx):
    return matrix.pop(row_idx)

def remove_col(matrix, col_idx):
    col = []
    
    for row in matrix:
        col.append(row.pop(col_idx))
    
    return col

def snail(snail_map):

    snail_map = snail_map.copy()
    
    output_list = []
    
    if len(snail_map) == 0:
        return []
    
    while True:

        output_list.extend(remove_row(snail_map,0))

        if len(snail_map) == 0:
            break

        output_list.extend(remove_col(snail_map,-1))

        if len(snail_map) == 0:
            break

        output_list.extend(remove_row(snail_map,-1)[::-1])

        if len(snail_map) == 0:
            break

        output_list.extend(remove_col(snail_map,0)[::-1])

        if len(snail_map) == 0:
            break

    return output_list


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array) == expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array) == expected)