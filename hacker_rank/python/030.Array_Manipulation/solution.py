#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # arr = [0 for i in range(n)]
    # for query in queries:
    #     start_idx = query[0] - 1
    #     end_idx = query[1] - 1
    #     val = query[2]
    #     for idx in range(start_idx, end_idx + 1):
    #         arr[idx] += val
    # return max(arr)
    arr = [0 for i in range(n+1)]
    for query in queries:
        arr[query[0]-1] += query[2]
        arr[query[1]] -= query[2]
    max_sum = 0
    tmp_sum = 0
    for v in arr:
        tmp_sum += v
        if tmp_sum > max_sum: max_sum = tmp_sum
    return max_sum
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
