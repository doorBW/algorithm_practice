#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    result = 0
    modify_q = [v-1 for v in q]
    for i,v in enumerate(modify_q):
        if v-i > 2:
            print("Too chaotic")
            return
        for j in range(max(v-1,0),i):
            if modify_q[j] > v:
                result += 1
    print(result)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
