#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys


def is_nested(line):
   print(line)


def main(args):
    """Open the input file and call `is_nested()` for each line"""
#    if len(sys.argv) != 2:
#         print 'usage: python nested.py file'
#         sys.exit(1)

    filename = sys.argv[1]
    with open (filename, 'r') as rf:
        file_lines = rf.readlines()
        for line in file_lines:
            is_nested(line)

if __name__ == '__main__':
    main(sys.argv[1:])
