#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    result = []
    for i in grades:
        if i < 38:
            result.append(i)
        else:
            if (i%5 == 0) or (i%5 == 1) or (i%5 == 2):
                result.append(i)
            else:
                result.append((i//5)*5 + 5)
    return result
    
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


