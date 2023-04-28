#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers)
"""

"""
def find_peak(list_of_integers):
    int_list = len(list_of_integers)
    peak_value = None
    if int_list == 0:
        peak_value = None
    elif int_list == 1:
        peak_value = list_of_integers[0]
    elif (int_list == 2) and (list_of_integers[0] >= list_of_integers[1]):
        peak_value = list_of_integers[0]
    elif (int_list == 2) and (list_of_integers[0] <= list_of_integers[1]):
        peak_value = list_of_integers[1]
    else:

        for i in range(int_list - 2):
            if (list_of_integers[i + 1] >= list_of_integers[i]) and\
                    (list_of_integers[i + 1] >= list_of_integers[i + 2]):
                peak_value = list_of_integers[i + 1]
    print(peak_value)
    print(list_of_integers[1:len(list_of_integers) - 1])
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    peak = None
    if len(list_of_integers) == 0:
        return peak
    else:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if peak <= i:
                peak = i
    return peak
