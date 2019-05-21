#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    sorted_a = list(sorted(a))
    cnt = 0
    while(a != sorted_a):
        for idx in range(len(a)-1):
            if(a[idx] > a[idx+1]):
                tmp = a[idx]
                a[idx] = a[idx+1]
                a[idx+1] = tmp
                cnt += 1
    print("Array is sorted in "+str(cnt)+" swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

