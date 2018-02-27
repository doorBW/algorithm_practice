#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    size = float(len(arr))
    plus = 0.0
    minus = 0.0
    zero = 0.0
    for i in arr:
        if i == 0:
            zero += 1.0
        elif i > 0:
            plus += 1.0
        else:
            minus += 1.0
    print("%0.6f" % (plus/size))
    print("%0.6f" % (minus/size))
    print("%0.6f" % (zero/size))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
