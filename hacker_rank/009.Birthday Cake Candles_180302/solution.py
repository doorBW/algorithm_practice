#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxNum = 0
    number = 0
    for i in ar:
        if i > maxNum:
            maxNum = i
    for i in ar:
        if i == maxNum:
            number += 1
    return number
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
