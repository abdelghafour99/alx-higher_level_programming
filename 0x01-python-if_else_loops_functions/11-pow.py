#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    for i in range(b):
        a*=a
    return a
