# The Coin Change Problem



해당 문제는 아래 주소에서 만나보실 수 있습니다.

**problem URL**: <https://www.hackerrank.com/challenges/coin-change/problem>



## 문제 풀이 코드

\#!/bin/python3

import math

import os

import random

import re

import sys

\# Complete the getWays function below.

def getWays(n, c):

​    change_arr = [1] + [0]*n

​    for coin in c:

​        for idx in range(coin,n+1):

​            change_arr[idx] += change_arr[idx-coin]

​    \# print(change_arr[n],end='')

​    return change_arr[n]

if __name__ == '__main__':

​    fptr = open(os.environ['OUTPUT_PATH'], 'w')

​    nm = input().split()

​    n = int(nm[0])

​    m = int(nm[1])

​    c = list(map(int, input().rstrip().split()))

​    \# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

​    ways = getWays(n, c)

​    fptr.write(str(ways) + '\n')

​    fptr.close()



## 문제 풀이 설명 및 후기

