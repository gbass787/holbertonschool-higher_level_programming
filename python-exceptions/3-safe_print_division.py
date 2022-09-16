#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0
    try:
        total = a / b
    except:
        total = None
    finally:
        print("Inside result: {}".format(total))
    return total
