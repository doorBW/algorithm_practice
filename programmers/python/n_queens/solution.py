answer = 0
N = 0
def calculate(arr):
    global answer, N
    r = len(arr)
    if r == N:
        answer += 1
        return
    for c in range(N):
        if c in arr:
            continue
        check = False
        for i,v in enumerate(arr):
            if abs(c - v) == abs(r - i):
                check = True
                break
        if not check:
            calculate(arr+[c])

def solution(n):
    global answer, N
    N = n
    calculate([])
    return answer

