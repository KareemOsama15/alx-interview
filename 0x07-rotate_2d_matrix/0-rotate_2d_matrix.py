#!/usr/bin/python3
"""Rotates 2-D matrix:"""


def rotate_2d_matrix(matrix):
    """Rotates in-place"""
    length = len(matrix)
    temp1, temp2 = 0, 0

    for j in range(0, len(matrix) // 2 + 1):
        for i in range(j, length - 1):
            temp1 = matrix[i][length - 1]
            matrix[i][length - 1] = matrix[j][i]
            temp2 = matrix[length - 1][length - 1 - i + j]
            matrix[length - 1][length - 1 - i + j] = temp1
            temp1 = matrix[length - 1 - i + j][j]
            matrix[length - 1 - i + j][j] = temp2
            matrix[j][i] = temp1
        length -= 1

# matrix = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]]

# rotate_2d_matrix(matrix)
# print(matrix)
