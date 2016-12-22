#!/bin/python2.7

import argparse
parser = argparse.ArgumentParser(description='Learn args test script')
parser.add_argument('-a1','--arg1',dest='a1',help='Description of current argument')
parser.add_argument('-a2','--arg2',dest='a2',help='Input file name')
parser.add_argument('-a3','--arg3',dest='a3',help='Input file name')
parser.add_argument('-a4','--arg4',dest='a4',help='Input file name')
parser.add_argument('-t','--type', help='type out information')

args = parser.parse_args()

print str(args.a1)
print str(args.a2)
print str(args.a3)
print str(args.a4)


