#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_tri(n):
    """Return the last list of lists"""

    m = 1
    l1 = [1]
    while n >= m:
        l2 = [1 for i in range(m)]
        for i in range(1, m-1):
            l2[i] = l1[i-1] + l1[i]
        l1 = l2
        m += 1
    return l1


def pascal_triangle(n):
    """The code"""

    if type(n) != int:
        raise TypeError("n should be an integer")
    if n <= 0:
        return [[]]
    else:
        return[pascal_tri(i) for i in range(1, n+1)]
