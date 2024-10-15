"""

In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by a list of lists.

Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any matrix can be transposed simply by switching columns with rows.

Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

Problem:
    Create a function that transposes a matrix that works with any MxN matrix

Rules:
    - Matrix must have at least one row and one columne
    - Any matrix can be transposed by switching rows and columns
    - Rows and columns are of different length

Examples:
    print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
    print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
    print(transpose([[1]]) == [[1]])

Algorihtm
- get length of first row in matrix and use it to detrmine the number of lists required in output matrix
- cycle through rows and columns and use column number for selecting row in matrix
- append item to that row
- return output_matrix

"""


def transpose(input_matrix):

    output_matrix = [[] for i in input_matrix[0]]

    for sublist in input_matrix:
        for idx,number in enumerate(sublist):
            output_matrix[idx].append(number)

    return output_matrix

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)