#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    val_lst = []
    i = 0
    while i < list_length:
        try:
            div_val = (my_list_1[i]/my_list_2[i])
        except TypeError:
            print("wrong type")
            div_val = 0
        except ZeroDivisionError:
            print("division by 0")
            div_val = 0
        except IndexError:
            print("out of range")
            div_val = 0
        finally:
            val_lst.append(div_val)
            i += 1
    return val_lst
