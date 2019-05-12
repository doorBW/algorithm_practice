#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = -100
    for i in range(1,5):
        for j in range(1,5):
            each_sum = 0
            each_sum += (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1])
            each_sum += arr[i][j]
            each_sum += (arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])
            if each_sum > result: result = each_sum
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

