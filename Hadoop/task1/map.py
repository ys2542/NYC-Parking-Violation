#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]
    
    if len(row) == 22:
        key = row[0]
        id = row[14]
        precinct = row[6]
        code = row[2]
        date = row[1]
        print(key + '\t' + id + ', ' + precinct + ', ' + code + ', ' + date)
    elif len(row) == 18:
        key = row[0]
        print(key + '\t' + 'Useless information')
