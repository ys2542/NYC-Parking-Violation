#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]
    make = row[20]
    color = row[19]
    if make == '':
        make = 'NONE'
    if color == '':
        color = 'NONE'
    print('a' + make + '\t' + '1')
    print('b' + color + '\t' + '1')
