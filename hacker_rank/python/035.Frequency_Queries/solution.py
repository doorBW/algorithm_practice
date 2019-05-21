#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    answer = ''
    f = Counter()
    c = Counter()
    for query in queries:
        if query[0] == 1:
            c[f[query[1]]] -= 1
            f[query[1]] += 1
            c[f[query[1]]] += 1
        elif query[0] == 2:
            if f[query[1]] > 0:
                c[f[query[1]]] -= 1
                f[query[1]] -= 1
                c[f[query[1]]] += 1
        else:
            if c[query[1]] > 0:
                answer += '1'
            else:
                answer += '0'
    return answer
    # answer = ''
    # 
    # dic = {}
    # for query in queries:
    #     if query[0] == 1:
    #         if query[1] in dic.keys():
    #             dic[query[1]] += 1

    #         else:
    #             dic[query[1]] = 1

    #     elif query[0] == 2:
    #         if (query[1] in dic.keys()) and dic[query[1]] > 0:
    #             dic[query[1]] -= 1
    #     else:
    #         if query[1] in dic.values():
    #             answer += '1'
    #         else:
    #             answer += '0'

    # return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

