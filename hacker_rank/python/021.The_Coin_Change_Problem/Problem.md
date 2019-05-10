# The Coin Change Problem



해당 문제는 아래 주소에서 만나보실 수 있습니다.

**problem URL**: <https://www.hackerrank.com/challenges/coin-change/problem>



## 문제 풀이 코드

\#!/bin/python3

import math

import os

import random

import re

import sys

\# Complete the getWays function below.

def getWays(n, c):

​    change_arr = [1] + [0]*n

​    for coin in c:

​        for idx in range(coin,n+1):

​            change_arr[idx] += change_arr[idx-coin]

​    \# print(change_arr[n],end='')

​    return change_arr[n]

if __name__ == '__main__':

​    fptr = open(os.environ['OUTPUT_PATH'], 'w')

​    nm = input().split()

​    n = int(nm[0])

​    m = int(nm[1])

​    c = list(map(int, input().rstrip().split()))

​    \# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

​    ways = getWays(n, c)

​    fptr.write(str(ways) + '\n')

​    fptr.close()



## 문제 -> 코드

문제에서 주어지는 다양한 코인을 통해 만들 수 있는 값을 1부터 시작한다.

즉 우리가 반환해야할 금액 1에 대해서 경우의 수를 찾기위해 어떻게 할 것인지를 생각해본다.

만약 1코인, 2코인, 3코인이 있다고 가정했을 때,

1에 대해서는 1코인 1개를 이용하는 1개의 방법뿐이다.

2에 대해서는 1코인 2개이용, 2코인 1개 이용하는 방법, 총 2가지가 존재한다.

3에 대해서는 1코인 3개이용, 3코인 1개이용, 1코인1개+2코인1개이용, 총3가지가 존재한다.

또한 각각의 코인에 대해서 나눠서 생각한다, 즉

1,2,3에 대해서 1코인만 이용했을때 그리고 2코인을 추가로 이용했을때, 등으로 나누어서 생각한다.

따라서 반환해야할 값에 대해 경우의 수를 저장하는 1차원 배열이 존재하고

각각의 코인에 대해 하나씩 반복하면서 배열에 경우의수를 늘려나가면 될 것이다.



## 문제 풀이 설명 및 후기

대표적인 dp문제 중에 하나이다.

예전에 대학에서 알고리즘 수업을 들을 때에도 관련된 문제를 공부한 적이 있는 것 같다.

처음에 초기화하는 change_arr 이 결국 dp에서 사용되는 테이블이라고 생각하면 된다.

반환해야 할 잔돈이 4일때 change_arr은 다음과 같이 초기화 된다.

[ 1, 0, 0, 0, 0 ]

여기서 각각의 숫자는 인덱스를 반환해야 할 잔돈으로 생각했을 때 가능한 경우의 수를 의미한다.

잘 이해가 되지 않는다면, 예를 들어 첫번째 코인 2로 확인을 해본다고 생각하자.

코인 2로 잔돈을 반환할 때 가능한 경우는 반환해야할 잔돈이 2일때 1가지방법, 반환해야할 잔돈이 4일때 1가지 방법이므로 위의 배열이

[ 1, 0, 1, 0, 1 ] 

이 될 것이다.

배열의 값이 무엇을 의미하는지 이해가 되었다면 다시 코드로 돌아가 for문부터 살펴보자.

첫번째 for문에서는 coin이 담겨져있는 c 리스트에서 하나씩 꺼내와서 판단한다

만약 코인 리스트가 [ 1, 2, 3 ] 이었다고 생각해보자. 그럼 첫번째 for문에서 coin = 1이 되고 두번째 포문을 반복하며 배열이 다음과 같이 변경될 것이다.

 [ 1, 0, 0, 0, 0 ] -> [ 1, 1, 1, 1, 1]

이제 다시 첫번째 for문으로 돌아와서 coin = 2가 되었다고 생각해보자.

그럼 두번째 포문을 통해 배열이 다음과 같이 변경된다.

 [ 1, 1, 1, 1, 1] -> [ 1, 1, 2, 2, 2 ]

위와 같은 과정을 통해 모든 코인에서 가능한 경우의 수를 더해가고

마지막에 우리가 알고자했던 위치의 값을 반환시키면 된다.

