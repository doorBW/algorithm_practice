#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    before_one_idx = 0
    try:
        while(c.index(1,before_one_idx) > 0):
            one_idx = c.index(1,before_one_idx)

            result += (one_idx - before_one_idx)//2

            before_one_idx = one_idx + 1
            result += 1
    except:
        if not before_one_idx == len(c) - 1:
            tmp = (len(c) - 1 - before_one_idx)//2
            if tmp == 0:
                result += 1
            else:
                result += tmp
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

