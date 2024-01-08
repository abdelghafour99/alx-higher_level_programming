#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """The Code"""

    a = len(matrix[0])
    mat = [[0 for i in range(a)] for j in range(len(matrix))]
    mes = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    for i in range(len(matrix)):
        if len(matrix[i]) != a:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError(mes)
            mat[i][j] = float(format(matrix[i][j] / div, ".2f"))
    return mat
