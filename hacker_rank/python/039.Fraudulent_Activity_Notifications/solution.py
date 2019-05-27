#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    m = 0
    c = 0
    for i,v in enumerate(expenditure):
        if i < d:
            m += v
        else:
            l = expenditure[i-d+1]
            if v >= 2*m/d:
                c += 1
            m += (v-l)

    return c

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

