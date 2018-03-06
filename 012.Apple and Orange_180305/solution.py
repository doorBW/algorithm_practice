#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    LarryScore = 0
    RobScore = 0
    temp = 0
    for i in apples:
        temp = i+a
        if (temp >= s) and (temp <= t):
            LarryScore += 1
    print(LarryScore)
    for i in oranges:
        temp = i+b
        if (temp >= s) and (temp <= t):
            RobScore += 1
    print(RobScore)
    
if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
