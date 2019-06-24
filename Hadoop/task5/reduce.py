#!/usr/bin/env python

import sys
import string

current_id = None
current_state = None
current_count = 0
greatest_count = 0
greatest_id = None
greatest_state = None

for line in sys.stdin:
    line = line.strip()
    id, info = line.split(', ', 1)
    state, count = info.split('\t', 1)
    count = int(count)
    
    if current_id == id and current_state == state:
        current_count = current_count + count
    else:
        if current_count > greatest_count:
            greatest_count = current_count
            greatest_id = current_id
            greatest_state = current_state
        current_count = count
        current_id = id
        current_state = state

print(greatest_id + ', ' + greatest_state + '\t' + str(greatest_count))            
