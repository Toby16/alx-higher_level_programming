#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
            count += 1
        except (ValueError, TypeError):
            i += 1
        except IndexError:
            raise
            i += 1
        # The below block of code isn't needed
        """else:
            pass
            i += 0"""
    print("")
    return count
