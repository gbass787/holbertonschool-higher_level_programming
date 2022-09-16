#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0, 0]
    for i in range(2):
        try:
            sum[i] += tuple_a[i]
        except:
            sum[i] += 0
        try:
            sum[i] += tuple_b[i]
        except:
            sum[i] += 0
    return tuple(sum)
