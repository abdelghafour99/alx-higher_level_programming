#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_tuple = [0, 0]
    for i in range(min(len(tuple_a), 2)):
        list_tuple[i] += tuple_a[i]

    for i in range(min(len(tuple_b), 2)):
        list_tuple[i] += tuple_b[i]

    return tuple(list_tuple)
