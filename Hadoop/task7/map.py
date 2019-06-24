#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]
    code = row[2]
    date = row[1]
    year, month, day = date.split('-', 2)
    weekend = (5, 6, 12, 13, 19, 20, 26, 27)
    weekday = (1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 28, 29, 30, 31)
    if int(day) in weekend:
        print(code + '\t' + 'weekend' + ' ' + '1.00')
    elif int(day) in weekday:
        print(code + '\t' + 'weekday' + ' ' + '1.00')
