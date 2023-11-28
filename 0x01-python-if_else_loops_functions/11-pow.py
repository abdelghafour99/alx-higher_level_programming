#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        for i in range(b):
            a*=a
    else:
        for i in range(b):
            a/=a
    return a
