#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            new_l = my_list.copy()
            new_l[idx] = element
            return new_l

