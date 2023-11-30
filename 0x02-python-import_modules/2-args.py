#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

S0 = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    S0 += 's.'
elif argc == 1:
    S0 += ':'
else:
    S0 += 's:'
print(S0.format(argc))


i = 0
for ar in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, ar))
    i += 1
