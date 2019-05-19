#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    cnt = 0
    arr = list(sorted(arr))
    if arr[0] == arr[-1]:
        return int(len(arr) * (len(arr)-1) * (len(arr)-2) / 6)

    arr_set = set(arr)
    arr_duplicated = list(sorted(list(arr_set)))
        
    for first_num in arr_duplicated:
        first_num_cnt = arr.count(first_num)
        
        second_num = first_num * r
        second_num_cnt = arr.count(second_num)
        if second_num_cnt == 0:
            continue
    
        third_num = second_num * r
        third_num_cnt = arr.count(third_num)
        if third_num_cnt == 0:
            continue
        
        cnt += first_num_cnt * second_num_cnt * third_num_cnt


    # for idx in range(len(arr)-2):
    #     second_list = [-1]
    #     first_num = arr[idx]

    #     second_num = first_num * r
    #     while True:
    #         third_list = [-1]
    #         if second_num in arr[second_list[-1]+1:]:
    #             second_list.append(arr.index(second_num,second_list[-1]+1))
    #             third_num = second_num * r
    #             while True:
    #                 if third_num in arr[third_list[-1]+1:]:
    #                     third_list.append(arr.index(third_num,third_list[-1]+1))
    #                     cnt += 1
    #                 else:
    #                     break
    #         else:
    #             break
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

