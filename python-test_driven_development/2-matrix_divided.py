#!/usr/bin/python3
'''File contains matrix_divided function'''


def matrix_divided(matrix, div):

    '''funtion divides all elements of a matrix of the same size'''

    new = []
    Error = "matrix must be a matrix (list of lists) of integers/floats"
    Error2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(Error)

    for row in matrix:
            if len(row) is not len(matrix[0]):
                raise TypeError(Error2)

    for row in matrix:
        for j in row:
            if type(j) not in [int, float]:
                raise TypeError(Error)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = (list(map(lambda x: list(map(lambda k: round(k / div,
                                                       2), x)), matrix)))
    return new
