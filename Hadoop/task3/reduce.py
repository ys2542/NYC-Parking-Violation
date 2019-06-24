#!/usr/bin/env python

import sys
import string

current_key = None
current_value = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, info = line.split('\t', 1)
    value, count = info.split(', ', 1)
    value = float(value)
    count = float(count)

    if key == current_key:
        current_count = current_count + count
        current_value = current_value + value
    else:
        if current_key:
            print(current_key + '\t' + "{0:.2f}".format(current_value) + ', ' + "{0:.2f}".format(current_value / current_count))
        current_count = count
        current_value = value
        current_key = key

if current_key == key:
    print(current_key + '\t' + "{0:.2f}".format(current_value) + ', ' + "{0:.2f}".format(current_value / current_count))
        
