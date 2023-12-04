#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if b > a:
        s = add(a, b)
        for j in range(4, 6):
            s = add(s, j)
        return (s)

    return sub(a, b)
