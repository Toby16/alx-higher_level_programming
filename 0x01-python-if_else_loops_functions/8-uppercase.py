#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        num = ord(i) - 32
        string += chr(num)
    print("{}".format(string))
