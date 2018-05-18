#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    sum_row = []
    sum_col = []
    number = len(container)
    # init
    for i in range(number):
        sum_row.append(0)
        sum_col.append(0)
        
    for i in range(number):
        for j in range(number):
            sum_row[i] += container[j][i]
            sum_col[i] += container[i][j]
    sum_row.sort()
    sum_col.sort()
    if sum_row != sum_col:
        return 'Impossible'
    
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

