#!/usr/bin/python3
for letter in range(90, 64, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter+32)), end="")
    else:
        print("{}".format(chr(letter)), end="")
