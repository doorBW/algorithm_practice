#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    dia_1 = 0
    dia_2 = 0
    max_num = len(a)
    for i in range(max_num):
        dia_1 += a[i][i]
        dia_2 += a[i][max_num -1 - i]
    if dia_1 >= dia_2:
        return dia_1 - dia_2
    else:
        return dia_2 - dia_1

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
