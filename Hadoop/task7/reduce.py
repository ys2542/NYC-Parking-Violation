#!/usr/bin/env python

import sys
import string

current_code = None
weekend_count = 0
weekday_count = 0

for line in sys.stdin:
    line = line.strip()
    code, info = line.split('\t')
    date, count = info.split(' ')
    count = float(count)
    
    if current_code == code:
        if date == 'weekend':
            weekend_count = weekend_count + count
        elif date == 'weekday':
            weekday_count = weekday_count + count
    else:
        if current_code:
            weekend_ave = weekend_count / 8.00
            weekday_ave = weekday_count / 23.00
            print(current_code + '\t' + "{0:.2f}".format(weekend_ave) + ', ' + "{0:.2f}".format(weekday_ave))
        current_code = code
        if date == 'weekend':
            weekend_count = count
            weekday_count = 0
        elif date == 'weekday':
            weekday_count = count
            weekend_count = 0
    
if current_code == code:
    weekend_ave = weekend_count/ 8.00
    weekday_ave = weekday_count/ 23.00
    print(current_code + '\t' + "{0:.2f}".format(weekend_ave) + ', ' + "{0:.2f}".format(weekday_ave))

