def solution(n, works):
    result=0 # 결과를 담을 변수
    works.append(0) # 최소값을 위해 works에 0추가
    works.sort() # works를 오름차순으로 정렬
    for i in range(1,len(works)): 
        # works에 대해 맨뒤에서 부터 확인할 것임
        # 인덱싱하기 편하게 하도록 i는 1부터 시작
        tmp = works[-i] - works[-(i+1)] # works에서 첫번째로 큰 숫자와 두번째로 큰 숫자의 차이 구함
        if tmp*i < n: # 해당 차이 x 몇번째인지가 n보다 작으면
            n -= tmp*i # 그만큼 n을 빼주고
            for j in range(1,i+1):
                works[-j] -= tmp # 첫번째로 큰 숫자를 두번째로 큰숫자와 같게 만든다.
        else: # 해당 차이 x 몇번째인지가 n보다 작은게 아니라면
            q = n//i # n에 대해서 몇번째인지로 나눈다. 이때 몫은 q, 나머지는 n
            n = n%i
            for j in range(1,i+1):
                works[-j] -= q # 제일 뒤의 숫자부터, i번째까지 몫만큼 빼준다.
            for j in range(1,n+1):
                works[-j] -= 1 # 나머지 처리
            break # 끝
    for i in works:
        result += i**2
        
    result = 0 # 결과를 담을 변수
    sumOfWorks = 0 # 모든 일의 합을 담을 변수
    for i in works: # 모든 일의 합을 구한다.
        sumOfWorks+=i 
    # 남은 일보다 n이 클때는 0을 반환
    if(n >= sumOfWorks): return 0

    # n이 0이될때 까지 반복
    while(n!=0):
        works[works.index(max(works))]-=1 # works에서 가장큰 값을 하나 줄이면서
        n-=1 # n의 값을 하나 줄인다.
        if(min(works) == max(works)): break
        # 만약 works에서 가장큰 값과 가장 작은 값이 같아지면 반복문을 나간다.

    # n이 0까지 줄어들어든 것이 아니라면
    if not n==0:
        # 이때는, works에서 가장큰값과 가장 작은 값이 같은 상황
        # 즉, works의 모든 값이 동일한 상황이다.
        # 따라서, n의 크기만큼의 요소를 -1씩해서 각각을 제곱하여 결과에 더하고
        # 나머지는 -1을 하지 않고 제곱해서 결과에 더한다.
        return n*((min(works)-1)**2) + (len(works)-n)*((min(works))**2)
    # n이 0까지 줄어든 것이라면 남은 works의 모든 값을 제곱해서 더한다.
    else:
        for i in works:
            result += i**2

    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
    return result