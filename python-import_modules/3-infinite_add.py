#!/usr/bin/python3
import sys

if __name__ == "__main__":

    sumOfAllArgv = 0

    if len(sys.argv) > 1:
        for count in range(1, (len(sys.argv))):
            sumOfAllArgv += int(sys.argv[count])

    print(sumOfAllArgv)
