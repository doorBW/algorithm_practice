T = int(input())
for test_case in range(T):
	cost = list(map(int,input().split()))
	table = list(map(int,input().split()))
	answer = [0]
    #1일 이용권만 이용
	for i in table:
		answer[0] += i
	answer[0] *= cost[0]
	#1달 이용권만 이용
	answer.append(cost[1]*12)
	#3달 이용권만 이용
	answer.append(cost[2]*4)
    #1년 이용권 이용
	answer.append(cost[3])
	tmp_s = 0
	count = 0
	n_table = []
	for days in table:
		n_table.append(min(days*cost[0],cost[1]))
	for _ in range(2):
		for idx,val in enumerate(n_table):
			if val == 0:
				continue
			elif count != 0:
				count -= 1
				continue
			else:
				if idx == 10:
					if cost[2] < (n_table[idx]+n_table[idx+1]):
						tmp_s += cost[2]
					else:
						tmp_s += (n_table[idx]+n_table[idx+1])
					break
				elif idx == 11:
					if cost[2] < val:
						tmp_s += cost[2]
					else:
						tmp_s += val
					break
				else:
					if cost[2] < (n_table[idx]+n_table[idx+1]+n_table[idx+2]):
						tmp_s += cost[2]
						count = 2
					else:
						tmp_s += val
		answer.append(tmp_s)
		n_table.reverse()
		tmp_s = 0
		count = 0
		
	print("#"+str(test_case+1)+" "+str(min(answer)))
