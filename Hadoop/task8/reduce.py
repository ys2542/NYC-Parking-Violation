#!/usr/bin/env python

import sys
import string

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)
    count = int(count)
    
    if current_key == key:
        current_count = current_count + count
    else:
        if current_key:
            if current_key[0] == 'a':
                print('vehicle_make' + '\t' + current_key[1:] + ', ' + str(current_count))
                #print('vehicle_make' + '\t' + current_key[1:] + ' ' + str(current_count))
            elif current_key[0] == 'b':
                print('vehicle_color' + '\t' + current_key[1:] + ', ' + str(current_count))
                #print('vehicle_color' + '\t' + current_key[1:] + ' ' + str(current_count))
        current_count = count
        current_key = key

if current_key == key:
    if current_key[0] == 'a':
        print('vehicle_make' + '\t' + current_key[1:] + ', ' + str(current_count))
        #print('vehicle_make' + '\t' + current_key[1:] + ' ' + str(current_count))
    elif current_key[0] == 'b':
        print('vehicle_color' + '\t' + current_key[1:] + ', ' + str(current_count))
        #print('vehicle_color' + '\t' + current_key[1:] + ' ' + str(current_count))
