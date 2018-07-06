#!/bin/python3

import math
import os
import random
import re
import sys


            
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    temp_score = 0
    
    #scores 에서 중복된 요소 제거
    for i in range(len(scores)-1):
        if scores[i] == scores[i+1]:
            scores[i] = -1
    remove_num = scores.count(-1)
    for _ in range(remove_num):
        scores.remove(-1)
        
    last_score = scores[len(scores)-1]
    
    # ----------------------------------
    

    for alice_score in alice:
        if alice_score < last_score:
            result.append(len(scores)+1)
            continue

        for index, item in enumerate(scores):
            if alice_score >= item:
                result.append(index+1)
                break
     
            
                
    return result
    
    # # 꼴찌 했을떄를 확인하기 위해 last score 기억
    # last_score = scores[len(scores)-1]
    # result = []
    # # alice의 각 점수에 따라서
    # for alice_score in alice:
#         # 초기 rank는 1로 설정
#         rank = 1
#         # 전의 스코어랑 같을 떄를 확인하기 위해 이전 스코어 값 기억
#         temp_score = 0
        
#         # scores의 각 점수에 따라서
#         for each_score in scores:
#             # 마지막 점수일때
#             if last_score == each_score:
#                 # alice 점수와 마지막 점수가 같다면 rank반환
#                 if alice_score == last_score:
#                     result.append(rank)
#                 # alice 점수가 마지막 점수보다 낮다면, rank+1 반환
#                 else:
#                     result.append(rank+1)
            
#             # 만약 alice점수가 더 높다면 현재 rank 반환하고 다음 alice점수 확인
#             elif alice_score >= each_score:
#                 result.append(rank)
#                 break
#             # alice 점수가 더 높은게 아니면 rank를 하나 올리는데,
#             # 이때 이전 점수와 현재 점수가 다를때만 하나 올림.
#             elif temp_score != each_score:
#                 rank += 1
#             # 이전 점수 기억
#             temp_score = each_score
#     return result
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

