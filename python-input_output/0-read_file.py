#!/usr/bin/python3
'''reads a text file'''


def read_file(filename=""):
    '''reads a text file'''
    with open(filename, encoding='UTF8') as f:
        for i in f:
            print(i, end='')
