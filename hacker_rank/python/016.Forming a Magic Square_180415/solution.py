#!/bin/python3

import sys

def formingMagicSquare(s):
    # Complete this function
    # Init var
    result = 0

    temp = [0,0,0,0,0,0,0,0,0]
    group = []
    counting = {}
    count_num = [[],[],[]]
    second_lines = []
    other_lines = []
    magic_square = []
    cost = 0
    minCost = 100

    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                if ((a+b+c) == 15)&(a != b)&(b != c)&(a != c):
                    k = sorted([a,b,c])
                    if k not in group:
                        group.append(k)
    
    for each in group:
        for i in range(0,3):
            if each[i] in counting:
                counting[each[i]] += 1
            else:
                counting[each[i]] = 1
    
    for key,value in counting.items():
        if value == 4:
            count_num[0].append(key)
        elif value == 3:
            count_num[1].append(key)
        elif value == 2:
            count_num[2].append(key)
    
    for line in group:
        if line[1] == 5:
            if (line[0] == 2)|(line[0] == 4)|(line[0] == 6)|(line[0] == 8):
                continue
            second_lines.append(line.copy())
            line[0], line[2] = line[2], line[0]
            second_lines.append(line)
        else:
            for i in line:
                if i in count_num[2]:
                    temp_line = line.copy()
                    temp_line.pop(temp_line.index(i))
                    temp_line.insert(1,i)
            other_lines.append(temp_line.copy())
            temp_line[0], temp_line[2] = temp_line[2], temp_line[0]
            other_lines.append(temp_line)
    
    other_lines_copy = other_lines.copy()
    for first_line in other_lines_copy:
        other_lines.pop(other_lines.index(first_line))
        for third_line in other_lines:            
            for second_line in second_lines:
                if (first_line[1] in second_line)|(third_line[1] in second_line):
                    continue
                elif ((first_line[0]+second_line[0]+third_line[0]==15)&(first_line[2]+second_line[2]+third_line[2]==15)&(first_line[0]+second_line[1]+third_line[2]==15)&(first_line[2]+second_line[1]+third_line[0]==15)):
                    magic_square.append(first_line+second_line+third_line)
        other_lines.append(first_line)
    # print(magic_square)
    # finish making magic square
    
    input_square = s[0]+s[1]+s[2]
    for test_square in magic_square:
        for i in range(0,9):
            cost += abs(test_square[i]-input_square[i])
        if minCost > cost:
            minCost = cost
        cost = 0
    return minCost
            
if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
