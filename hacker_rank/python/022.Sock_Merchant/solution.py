#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result = 0
    # First Code
    # socks_dic = {}
    # for each in ar:
    #     if each in socks_dic.keys():
    #         socks_dic[each] += 1
    #     else:
    #         socks_dic[each] = 1
    
    # for each in socks_dic.keys():
    #     if socks_dic[each] >= 2:
    #         result += socks_dic[each]//2

    # Second Code using comprehension
    for num in [len(list(g)) for k, g in groupby(sorted(ar))]:
        result += num//2

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

