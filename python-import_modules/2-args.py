#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("0 arguments.")

    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(((len(sys.argv)) - 1), sys.argv[1]))

    else:
        print("{} arguments:".format(len(sys.argv) - 1))

        for count in range(1, (len(sys.argv))):
            print("{:d}:".format(count), sys.argv[count])
