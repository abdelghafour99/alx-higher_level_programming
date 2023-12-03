#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_tuple = [0, 0]
    for i in range(len(tuple_a)):
        list_tuple[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        list_tuple[i] += tuple_b[i]

    return tuple(list_tuple)
