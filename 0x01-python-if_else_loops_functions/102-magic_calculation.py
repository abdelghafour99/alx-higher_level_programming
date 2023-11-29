#!/usr/bin/python3

def magic_calculation(a, b, c):
    if c > b:
        return a + b
    elif b > a:
        return c
    return a * b - c
