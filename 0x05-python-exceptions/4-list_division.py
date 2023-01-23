#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    val_lst = []
    i = 0
    while i < list_length:
        try:
            div_val = my_list_1[i]/my_list_2[i]
            i += 1
        except (TypeError):
            print("wrong type")
            div_val = 0
            i += 1
        except ZeroDivisionError:
            print("division by zero")
            div_val = 0
            i += 1
        except IndexError:
            print("out of range")
            div_val = 0
            i += 1
        finally:
            val_lst.append(div_val)
    return val_lst
