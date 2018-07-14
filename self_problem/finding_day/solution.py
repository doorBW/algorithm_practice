
# 함수이름 수정하지 말 것
# don't modify function name
def your_answer(y,m,d):
	# 하단에 코드를 작성하세요
	# write your code

	day_dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN' }
	standard_year = [31,28,31,30,31,30,31,31,30,31,30,31]

	standard_year_sum_day = 0
	for i in standard_year:
		standard_year_sum_day += i

	special_year = [31,29,31,30,31,30,31,31,30,31,30,31]
	special_year_sum_day = 0
	for i in special_year:
		special_year_sum_day += i

	first_day = 0
	sum_day = first_day

	for year in range(1,y+1):
		if year == y:
			if year % 4 == 0: # 윤년
				if year % 100 == 0: # 평년
					if year % 400 == 0: # 윤년
						for month in range(m-1):
							sum_day += special_year[month]
					else:
						for month in range(m-1):
							sum_day += standard_year[month]
				else:
					for month in range(m-1):
						sum_day += special_year[month]
			else:
				for month in range(m-1):
					sum_day += standard_year[month]
			sum_day += d-1
		else:
			if year % 4 == 0: # 윤년
				if year % 100 == 0: # 평년
					if year % 400 == 0: # 윤년
						sum_day += special_year_sum_day
					else:
						sum_day += standard_year_sum_day
				else:
					sum_day += special_year_sum_day
			else:
				sum_day += standard_year_sum_day

	result = day_dic[sum_day % 7]

	# 반환값은 다음과 같은 형식이어야 합니다.
	# The return value must be in the following format
	return result # MON, TUE, ...
