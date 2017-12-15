#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt, time, os
from Power import Controller

SingleTime = 5
#单次运行时间

def main(argv):
    runtime = ''
    try:
        opts, args = getopt.getopt(argv, "ht:", ["ifile="])
    except getopt.GetoptError:
        print 'test.py -t <runtime>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -t <runtime> '
            sys.exit()
        elif opt in ("-t", "--ifile"):
            runtime = arg
    return runtime

if __name__ == '__main__':
    run_count = main(sys.argv[1:])
