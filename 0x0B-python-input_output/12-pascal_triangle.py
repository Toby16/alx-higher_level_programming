#!/usr/bin/python3
""""
module containing function that returns a list of lists of integers
representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    creats the pascal triangle
    Arguments:
        n: create pascal triangle up to n
    """
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    return result
