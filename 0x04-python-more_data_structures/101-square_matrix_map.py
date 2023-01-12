#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    val_ = list(map(lambda y: list(map(lambda x: x ** 2, y)), matrix))
    return (val_)
