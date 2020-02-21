#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Justin Miller"
# Time to completed:  1 hour
# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# referenced for building is_nested function arch

import sys



def is_nested(line):
    left_side =  ["[","{","("]
    right_side = ["]","}",")"]
    unmatched_list = []
    error = 0
    for char in line:
        if char in left_side:
            unmatched_list.append(char)
        elif char in right_side:
            loc = right_side.index(char)
            if((len(unmatched_list)) > 0) and (left_side[loc] == unmatched_list[len(unmatched_list)-1]):
                unmatched_list.pop()
            else:
                error = line.index(char)
                print("NO " + str(error))
    if len(unmatched_list) != 0:
        print("No " + str((len(line))+1))
    elif len(unmatched_list) == 0 and error == 0:
        print("YES")

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    filename = sys.argv[1]
    with open (filename, 'r') as rf:
        file_lines = rf.readlines()
        for line in file_lines:
            is_nested(line)

if __name__ == '__main__':
    main(sys.argv[1:])
