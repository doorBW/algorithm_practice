
def solution(A, K):
    # write your code in Python 3.6
    result = []
    K = K%len(A)
    count = len(A) - K
    if K == 0:
        return A
    
    for k in range(len(A)):
        result.append(A[count])
        count += 1
        count %= len(A)
    return result
