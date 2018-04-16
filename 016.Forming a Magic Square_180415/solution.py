#!/bin/python3

import sys

def formingMagicSquare(s):
    # Complete this function
    # print(s) -> [[],[],[]]
    # We have to check the magic number.
    ## How can we know the magic number??? => just counting
    ## um...
    # And, checking each line's sum is same with the magic number.
    # Different line calculate the cost
    # sum cost..
    
    # Init var
    result = 0
    row = []
    col = []
    dia = []
    sum_list = {}
    magic_number = 0
    temp = 0
    for i in range(0,3):
        row_temp = 0
        col_temp = 0
        for j in range(0,3):
            row_temp += s[i][j]
            col_temp += s[j][i]
        row.append(row_temp)
        col.append(col_temp)
    dia.append(s[0][0]+s[1][1]+s[2][2])
    dia.append(s[0][2]+s[1][1]+s[2][0])
    for i in row:
        if i in sum_list:
            sum_list[i] += 1
        else:
            sum_list[i] = 1
    for i in col:
        if i in sum_list:
            sum_list[i] += 1
        else:
            sum_list[i] = 1
    for i in dia:
        if i in sum_list:
            sum_list[i] += 1
        else:
            sum_list[i] = 1
                
    # decide magic number
    for i in sum_list.values():
        if i > temp:
            temp = i
    for key, value in sum_list.items():
        if value == temp:
            magic_number = key
    
    while (1):
        if (row[0] == row[1] == row[2] == col[0] == col[1] == col[2] == dia[0] == dia[1]):
            return result
        
        break
    print("##")
    
    
if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
