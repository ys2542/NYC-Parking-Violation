#!/usr/bin/env python

import sys
import string

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    count = int(value)
    
    if current_key == key:
        current_count = current_count + count
    else:
        if current_key:
            print(current_key + '\t' + str(current_count))
        current_count = count
        current_key = key

if current_key == key:
    print(current_key + '\t' + str(current_count))
            
