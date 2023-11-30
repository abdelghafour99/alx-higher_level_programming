#!/usr/bin/python3
import sys
import hidden_4 as hid

if __name__ != "__main__":
    exit()

for ar in dir(hid):
    if ar[0:2] != "__":
        print(ar)
