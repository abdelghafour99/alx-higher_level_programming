#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    c = [0 ,0]
    if len(tuple_b) > 1:
        c[0] = a[0] + b[0]
        c[1] = a[1] + b[1]
    elif len(tuple_b) == 1:
        c[0] = a[0] + b[0]
        c[1] = a[1]
    elif len(tuple_b) == 0:
        c[0] = a[0]
        c[1] = a[1]
    return tuple(c)
