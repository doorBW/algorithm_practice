#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    result = 0
    now = 0
    can_vally = 0
    before_step = ''
    for i,step in enumerate(s):
        # first step
        if before_step == '':
            if step == 'U':
                now += 1
                before_step = 'U'
            else:
                now -= 1
                before_step = 'D'
                can_vally = 1
        
        # Second step ~
        elif step == 'U':
            if before_step == 'U':
                pass
            else: # 내려가다가 올라가는 상황
                if now < 0:
                    can_vally = 1
                else:
                    pass
            now += 1
            before_step = 'U'
        else:
            if before_step == 'D':
                pass
            else: # 올라가다가 내려가는 상황
                if now >= 0:
                    if can_vally == 1:
                        result += 1
                else:
                    pass
                can_vally = 0
            now -= 1
            before_step = 'D'

    if before_step == 'U':
        if now>=0 and can_vally==1:
            result += 1
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

