#!/usr/bin/python3
for i in range(0, 100):
    if ((i < 10) or (i >= 10)) and (i != 99):
        print("{0:0=2d}".format(i), end=", ")
    elif i == 99:
        print("{0:0=2d}".format(i))
