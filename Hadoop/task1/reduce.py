#!/usr/bin/env python

import sys
import string

current_key = None
current_values = None
count = 0

for line in sys.stdin:
    line = line.strip()
    key, values = line.split('\t', 1)
    
    if current_key == key:
        count = count + 1
    else:
        if current_key:
            if count == 1:
                if current_values != 'Useless information':
                    print(current_key + '\t' + current_values)

        current_key = key
        count = 1
        current_values = values

if count == 1:
    if values != 'Useless information':
        print(key + '\t' + values)
