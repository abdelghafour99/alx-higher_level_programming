#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

S = 0
i = 0

for ar in sys.argv:
    if i != 0:
        S += int(ar)
    else:
        i += 1
print("{:d}".format(S))
