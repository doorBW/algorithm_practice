import math
import os
import random
import re
import sys

def getWays(n,c):
    change_arr = [1] + [0]*n
    for coin in c:
        for idx in range(coin,n+1):
            change_arr[idx] += change_arr[idx-coin]
    return change_arr[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))

    ways = getWays(n,c)
    fptr.write(str(ways) + '\n')
    fptr.close()
