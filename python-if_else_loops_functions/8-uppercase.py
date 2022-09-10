#!/usr/bin/python3
def uppercase(str):

    lengthOfString = len(str)

    for count in range(lengthOfString):
        if ord(str[count]) > 96:
                upperCaseLetter = chr(((ord(str[count])) - 32))
        else:
            upperCaseLetter = str[count]

        print("{}".format(upperCaseLetter), end="")

    print("")
