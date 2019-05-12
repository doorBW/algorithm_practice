#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    num = 0
    cnt = 0
    while(1):
        if cnt == len(arr)-1: break
        cnt += 1
        if arr[cnt-1] == cnt: continue
        else:
            tmp = arr[arr[cnt-1]-1]
            arr[arr[cnt-1]-1] = arr[cnt-1]
            arr[cnt-1] = tmp
            num += 1
            cnt -= 1
        
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

