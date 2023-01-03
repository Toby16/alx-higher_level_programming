#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(i) - 32
        elif i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or "abcdefghijklmnoqrstuvwxyz":
            num = ord(i)
        else:
            num = ord(i)
        string += chr(num)
    print("{}".format(string))
