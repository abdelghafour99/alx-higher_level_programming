#!/usr/bin/python3
def weight_average(my_list=[]):
    a, b = 0, 0
    if my_list:
        for i in my_list:
            a += (i[0] * i[1])
            b += i[1]
        a /= b
    return a
