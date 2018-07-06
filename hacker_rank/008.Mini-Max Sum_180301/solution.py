#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    sum = 0
    maxNum = arr[1]
    minNum = arr[1]
    for i in arr:
        sum += i
        if maxNum < i:
            maxNum = i
        if minNum > i:
            minNum = i
    minAdd = sum - maxNum
    maxAdd = sum - minNum
    print(minAdd, maxAdd)
    
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
