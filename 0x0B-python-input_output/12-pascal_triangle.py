#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_tri(n):
    """Return the last list of lists"""

    if n == 1:
        return [1]
    else:
        lis = [1 for i in range(n)]
        for i in range(1, n-1):
            lis[i] = pascal_tri(n-1)[i-1] + pascal_tri(n-1)[i]
    return lis


def pascal_triangle(n):
    """The code"""

    if type(n) != int:
        raise TypeError("n should be an integer")
    if n <= 0:
        return []
    else:
        return[pascal_tri(i) for i in range(1, n+1)]
