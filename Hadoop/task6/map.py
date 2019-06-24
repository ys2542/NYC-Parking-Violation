#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    line = line.strip()
    row = csv.reader([line], delimiter = ',')
    row = list(row)[0]
    id = row[14]
    state = row[16]
    print(id + ', ' + state + '\t' + '1')
