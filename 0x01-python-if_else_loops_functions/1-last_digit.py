#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = int(str(number)[-1])
s = "Last digit of {} is {} and is {}"
s1 = "greater than 5"
s2 = "0"
s3 = "less than 6 and not 0"
if number < 0:
    n = -n
if n > 5:
    print(s.format(number, n, s1))
elif n == 0:
    print(s.format(number, n, s2))
elif n < 6:
    print(s.format(number, n, s3))
