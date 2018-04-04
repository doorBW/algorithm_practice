#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    # Write your code here.
    result = []
    high = score[0]
    low = score[0]
    high_count = 0
    low_count = 0
    for i in score[1:]:
        if i > high:
            high = i
            high_count += 1
        if i < low:
            low = i
            low_count += 1
    result.append(high_count)
    result.append(low_count)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
