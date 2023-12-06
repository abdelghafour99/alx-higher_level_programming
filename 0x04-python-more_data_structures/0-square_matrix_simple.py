#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nem = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            nem[i][j] = matrix[i][j] * matrix[i][j]
    return nem
