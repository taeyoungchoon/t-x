#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    fn = sys.argv[1]
else:
    exit(0)

input = open(fn)
lines = input.readlines()
for line in lines:
    print(line.rstrip())

