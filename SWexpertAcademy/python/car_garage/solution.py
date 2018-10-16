T = int(input())
for test_num in range(1,T+1):
	N, M, K, A, B = list(map(int,input().split()))
	ai = list(map(int,input().split()))
	bi = list(map(int,input().split()))
	t = list(map(int,input().split()))
    # - - - - - input end
	target = str(A)+str(B)
	max_time = max(t)+max(ai)+max(bi)
    #print("target:",target,"/ max time:",max_time)
    # - - - - - calculate start
	answer = 0
	time = min(t)
	reception_wait_list = []
	reception_list = [-1 for _ in range(N)]
	reception_time_list = [-1 for _ in range(N)]

	repair_wait_list = []
	repair_list = [-1 for _ in range(M)]
	repair_time_list =  [-1 for _ in range(M)]

	done_list = []
	people_dic = {}
	while(len(done_list) < len(t)):
#		print("반복 시작 현재 time:",time)
    #	print("first: 외부 사람 -> 접수 대기 리스트",t)
        # first: 외부 사람 -> 접수 대기 리스트
		for i,v in enumerate(t):
			if v == time:
				reception_wait_list.append(i)

#		print("second: 접수 리스트 -> 정비 대기 리스트")
        # second: 접수 리스트 -> 정비 대기 리스트
		for i,v in enumerate(reception_time_list):
			if v == 0:
				repair_wait_list.append(reception_list[i])
				reception_list[i] = -1
				reception_time_list[i] = -1

    #	print("third: 접수 대기 리스트 -> 접수 리스트")
        # third: 접수 대기 리스트 -> 접수 리스트
		for i in reception_wait_list:
			if -1 in reception_list:
				for idx,val in enumerate(reception_list):
					if val == -1:
						reception_list[idx] = i
						people_dic[i+1] = str(idx+1)
						reception_time_list[idx] = ai[idx]
						break
			else:
				break
		for tmp in reception_list:
			if tmp in reception_wait_list:
				reception_wait_list.remove(tmp)

#		print("4th: 정비 리스트 -> 끝")
        #4th: 정비 리스트 -> 끝
		for i,v in enumerate(repair_time_list):
			if v == 0:
				done_list.append(repair_list[i])
				repair_list[i] = -1
				repair_time_list[i] = -1

#		print("5th: 정비 대기 리스트 -> 정비 리스트")
        #5th: 정비 대기 리스트 -> 정비 리스트
		for i in repair_wait_list:
			if -1 in repair_list:
				for idx,val in enumerate(repair_list):
					if val == -1:
						repair_list[idx] = i
						people_dic[i+1] += str(idx+1)
						repair_time_list[idx] = bi[idx]
						break
			else:
				break
		for tmp in repair_list:
			if tmp in repair_wait_list:
				repair_wait_list.remove(tmp)
                
#		print("시간 증가 및 접수&정비 시간 리스트에서 0 초과 요소들 1 감소")
        # 시간 증가 및 접수&정비 시간 리스트에서 0 초과 요소들 1 감소
		time += 1
		for idx,val in enumerate(reception_time_list):
			if val > 0:
				reception_time_list[idx] -= 1

		for idx,val in enumerate(repair_time_list):
			if val > 0:
				repair_time_list[idx] -= 1
        #print("반복 한번 완료 이제 time:",time)
    # - - - - - calculate end
	for key,val in people_dic.items():
		if val == target:
			answer += key
	
    # - - - - - print answer
	if(answer == 0):
		print("#"+str(test_num)+" "+str(-1))
	else:
		print("#"+str(test_num)+" "+str(answer))
