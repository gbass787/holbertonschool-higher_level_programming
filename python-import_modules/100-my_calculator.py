#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    length = len(argv)
    arg = argv
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(arg[1])
    b = int(arg[3])
    sign = arg[2]

    if sign == "+":
        d = add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, d))
    elif sign == "-":
        d = sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, d))
    elif sign == "*":
        d = mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, d))
    elif sign == "/":
        d = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, d))
    else:
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)
