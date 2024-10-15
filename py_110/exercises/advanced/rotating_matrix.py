"""
As we saw in the previous exercises, a matrix can be represented by a list of lists. For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6
is represented by the following list of list:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

A 90-degree rotation of a matrix produces a new matrix in which each side of the matrix is rotated clockwise by 90 degrees. 
For example, the 90-degree rotation of the matrix shown above is:

3  4  1
9  7  5
6  2  8
A 90-degree rotation of a non-square matrix is similar. For example, given the following matrix:

3  4  1
9  7  5
its 90-degree rotation is:

9  3
7  4
5  1
Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. 
The function should not mutate the original matrix.

Probelm:
    - Write a function that takes and MxN matrix and rotates it clockwise by 90-degrees

Rules:
    - The function should not mutate the original matrix
    - All matrices contain values
    - Matrices may have unequal number of rows and columns

Examples:
    - First row becomes last column
    - second row becomes second clumn
    - last row becomes first column

Algorithm:
    - Build empty matrix and populate with empty lists to match length of first row of matrix
    - iterate through rows in reverse:
        - add first item of row to first list
        - add second item of row to second list
        - add third item of row to third list
        - move to next row until all rows are complete
    - return out_matrix

"""

def rotate90(input_matrix):

    output_matrix = [[] for item in input_matrix[0]]

    for sublist in input_matrix[::-1]:
        for idx,number in enumerate(sublist):
            output_matrix[idx].append(number)
        
    return output_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

