#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = [0 ,0]
    for i in range(len(tuple_a)):
        l[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        l[i] += tuple_b[i]

    return tuple(l)
