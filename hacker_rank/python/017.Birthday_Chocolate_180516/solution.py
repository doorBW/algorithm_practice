#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    start = 0
    start_temp = 0
    result = 0
    for _ in range(n):
        sum_temp = 0
        start_temp = start
        for _ in range(m):
            sum_temp += s[start_temp]
            start_temp += 1
            if start_temp >= n:
                break
        if sum_temp == d:
            result += 1
        start += 1
    return result
            
            
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
