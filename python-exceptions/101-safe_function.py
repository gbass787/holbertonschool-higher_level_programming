#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    total = None
    try:
        total = fct(*args)
        return total
    except:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return total
