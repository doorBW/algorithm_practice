#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    # Write your code here.
    result = []
    sw = 1
    
    b_min = 101
    for i in b:
        if i < b_min:
            b_min = i
            
    a_max = 0
    for i in a:
        if i > a_max:
            a_max = i    
    for i in range(a_max,b_min+1):
        sw = 1
        for a_i in a:
            if i%a_i == 0:
                pass
            else:
                sw = 0
        for b_i in b:
            if b_i%i == 0:
                pass
            else:
                sw = 0
        if sw == 1:
            result.append(i)
    return len(result)
        
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
