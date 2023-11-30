#!/usr/bin/python3
import hidden_4 as hid

if __name__ != "__main__":
    for ar in dir(hid):
        if ar[0] != "_" or ar[1] != "_":
            print(ar)
