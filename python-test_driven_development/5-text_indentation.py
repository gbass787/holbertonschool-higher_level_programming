#!/usr/bin/python3
'''function that prints text divided into new lines'''


def text_indentation(text):
    '''prints text in new lines'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    checker = 0
    for i in text:
        if i == " " and checker == 1:
            continue
        print(i, end="")
        checker = 0
        if i in [".", "?", ":"]:
            print("\n")
            checker = 1
