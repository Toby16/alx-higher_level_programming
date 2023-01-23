#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    val_lst = []
    for i in range(0, list_length):
        try:
            val_lst.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            print("wrong type")
            val_lst.append(0)
        except ZeroDivisionError:
            print("division by zero")
            val_lst.append(0)
        except IndexError:
            print("out of range")
            val_lst.append(0)
        finally:
            pass
    return val_lst
