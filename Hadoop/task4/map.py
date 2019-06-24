#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]

    if row[16] == 'NY':
        key = row[16]
    else:
        key = 'Other'

    print(key + '\t' + '1')
