#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    cnt = 0
    hash_dic = {}
    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            tmp_s = s[j:j+i]
            hash_s = 0

            for each in tmp_s:
                hash_s += hash(each)

            if hash_s in hash_dic.keys():
                hash_dic[hash_s] += 1
            else:
                hash_dic[hash_s] = 1

    for k,v in hash_dic.items():
        if v > 1:
            tmp = v*(v-1)//2
            cnt += tmp
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
