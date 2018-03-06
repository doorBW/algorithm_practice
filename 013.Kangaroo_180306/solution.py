#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    loc1 = x1
    loc2 = x2
    if v1 <= v2:
        return "NO"
    else:
        while loc2 > loc1:
            loc1 += v1
            loc2 += v2
            if loc1 == loc2:
                return "YES"
        return "NO"
    
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
