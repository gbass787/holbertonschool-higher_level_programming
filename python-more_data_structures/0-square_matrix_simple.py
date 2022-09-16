#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new.append(list(map(lambda x: x**2, matrix[i])))
    return new
