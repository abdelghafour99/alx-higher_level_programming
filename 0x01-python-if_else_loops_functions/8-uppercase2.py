#!/usr/bin/python3
def uppercase(str):
    a="abcdefghijklmnopqrstuvwxyz"
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(str)):
        d=0
        for j in range(len(a)):
            if str[i] == a[j]:
                print("{}".format(A[j]), end="")
                d=1
        if d == 0: 
            print("{}".format(str[i]), end="")
    print("")
