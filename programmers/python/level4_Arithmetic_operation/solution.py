# max와 min이 계산된 식에 대해서 바로 값을 알 수 있도록 함
max_dic = {}
min_dic = {}

def solution(arr):
    answer = 1
    # arr을 최대화
    answer = maximize(arr)
    return answer

def maximize(arr):
    # 길이가 1이면 요소 자체가 max or min 임
    if len(arr) == 1:
        return int(arr[0])
    tmp_tuple = tuple(arr)
    # arr(tmp_tuple)이 이미 계산된 적이 있다면 바로 반환
    if tmp_tuple in max_dic:
        return max_dic[tmp_tuple]
    
    max_n = -100001
    for i in range(1,len(arr),2): # 0번째 요소는 숫자임. 1번째 요소가 기호이고, 기호만 확인하면 됨
        if arr[i] == '+':
            n = maximize(arr[:i]) + maximize(arr[i+1:])
            if max_n < n:
                max_n = n
        else:
            n = maximize(arr[:i]) - minimize(arr[i+1:])
            if max_n < n:
                max_n = n
    max_dic[tmp_tuple] = max_n
    return max_n
    
def minimize(arr):
    # 길이가 1이면 요소 자체가 max or min 임
    if len(arr) == 1:
        return int(arr[0])
    tmp_tuple = tuple(arr)
    # arr(tmp_tuple)이 이미 계산된 적이 있다면 바로 반환
    if tmp_tuple in min_dic:
        return min_dic[tmp_tuple]
    
    min_n = 100001
    for i in range(1,len(arr),2): # 0번째 요소는 숫자임. 1번째 요소가 기호이고, 기호만 확인하면 됨
        if arr[i] == '+':
            n = minimize(arr[:i]) + minimize(arr[i+1:])
            if min_n > n:
                min_n = n
        else:
            n = minimize(arr[:i]) - maximize(arr[i+1:])
            if min_n > n:
                min_n = n
    min_dic[tmp_tuple] = min_n
    return min_n
