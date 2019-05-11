#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = 0
    a_num_in_s = 0
    for each in s:
        if each == 'a': a_num_in_s += 1
    
    s_len = len(s)
    result = a_num_in_s * (n//s_len)
    if n%s_len != 0:
        for each in s[0:n%s_len]:
            if each == 'a': result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

