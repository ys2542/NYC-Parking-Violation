#!/usr/bin/env python

import sys
import string

current_key = None
current_count = 0
idstate_number = {}

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    count = int(count)
    
    if current_key == key:
        current_count = current_count + count
    else:
        if current_key:
            idstate_number.update({current_key:current_count})
        current_count = count
        current_key = key

sorted_idstate_number = sorted(idstate_number.items(), key = lambda x: (-x[1], x[0]))    

for i in range(20):
    print(sorted_idstate_number[i][0] + '\t' + str(sorted_idstate_number[i][1]))
