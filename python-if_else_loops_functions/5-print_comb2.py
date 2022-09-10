#!/usr/bin/python3
for count in range(100):
    if count != 99:
        print("{0:02d}".format(count), end=", ")
    elif count == 99:
        print("{:d}".format(count))i
