#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    hour = int(s[0:2])
    check = s[8:10]
    strHour = ''
    if (check == 'PM')&(hour == 12):
        strHour = str(hour)
    elif (check == 'AM'):
        if hour == 12:
            hour += 12
        strHour = str(hour)
    else:
        hour += 12
        strHour = str(hour)
    if hour >= 24:
        hour -= 24
        strHour = str(hour)
    if hour <= 9:
        strHour = '0'+str(hour)
    newTime = strHour+s[2:8]
    return newTime
s = input().strip()
result = timeConversion(s)
print(result)
