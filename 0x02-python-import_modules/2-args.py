#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 0
    print("{:d} arguments:".format(len(sys.argv[1:])))
    for i in sys.argv[1:]:
        j += 1
        print("{:d}: {:s}".format(j, i))
