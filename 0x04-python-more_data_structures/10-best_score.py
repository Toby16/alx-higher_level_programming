#!/usr/bin/python3
def best_score(a_dictionary):
    max_val_n = 0
    max__val_k = None

    if a_dictionary is not None:
        for k in a_dictionary:
            if a_dictionary[k] > max_val_n:
                max_val_k = k
                max_val_n = a_dictionary[k]
    return max_val_k
