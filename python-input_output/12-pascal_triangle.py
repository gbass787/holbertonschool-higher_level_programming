#!/usr/bin/python3
'''returns a list of pascal triangle'''


def pascal_triangle(n):
    '''returns a list of pascal triangle'''

    lists = [[1]]
    if n == 0:
        return []

    for x in range(1, n):
        pascal = []
        for i in range(x + 1):
            if i == 0:
                pascal.append(1)
                continue
            if i == x:
                pascal.append(1)
                continue
            pascal.append(lists[x - 1][i - 1] + lists[x - 1][i])
        lists.append(pascal)
    return lists
