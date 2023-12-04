#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for a in matrix:
            for i in range(len(a)-1):
                print("{:d} ".format(a[i]), end="")
            if a:
                print("{:d}".format(a[-1]))
