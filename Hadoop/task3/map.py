#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]
    key = row[2]
    
    if row[12]:
        value = float(row[12])
    else:
        value = float(0.00)
    
    print(key + '\t' + str(value) + ', ' + '1.00')
     
