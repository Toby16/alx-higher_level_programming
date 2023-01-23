#!/usr/bin/python3
def safe_print_division(a, b):
    div_val = None
    try:
        div_val = a/b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(div_val))
    return div_val
