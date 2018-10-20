T = int(input())
for test_case in range(T):
	number_dic = {}
	N,K = map(int,input().split())
	input_num = input()
	input_num = input_num.strip()
	each_n = N//4
	for _ in range(each_n):
		tmp_num = ''
		each_num_list = []
		for i in range(4):
			each_num_list.append(input_num[i*each_n:(i+1)*each_n])
		for each in each_num_list:
			tmp = 0
			sum_each = 0
			for k in range(1,each_n+1):
				try:
					tmp = int(each[-k])
				except:
					if each[-k] == 'A':
						tmp = 10
					elif each[-k] == 'B':
						tmp = 11
					elif each[-k] == 'C':
						tmp = 12
					elif each[-k] == 'D':
						tmp = 13
					elif each[-k] == 'E':
						tmp = 14
					elif each[-k] == 'F':
						tmp = 15
				sum_each += tmp*(16**(k-1))
			number_dic[each] = sum_each
		tmp_num = input_num
		input_num = tmp_num[-1] + tmp_num[:-1]
	key_list = list(number_dic.values())
	key_list.sort()
	print("#"+str(test_case+1)+" "+str(key_list[-K]))
