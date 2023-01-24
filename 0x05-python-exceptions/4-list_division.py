#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    val_lst = []
    div_val = 0
    for i in range(0, list_length):
        try:
            div_val = (my_list_1[i]/my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
            div_val = 0
        except IndexError:
            print("out of range")
        finally:
            val_lst.append(div_val)
    return val_lst
