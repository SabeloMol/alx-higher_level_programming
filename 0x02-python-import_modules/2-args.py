#!/usr/bin/python3

"""calculates the number of arguments"""
import sys

def print_arguments():
    num_args = len(sys.argv) - 1
    
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1.")
        print("1: {}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}.".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    print_arguments()

