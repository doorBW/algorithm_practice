import datetime
import solution

def checking_answer(y,m,d,user_answer):
	day_dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN' }
	day_num = datetime.date(y,m,d).weekday()
	print(day_dic[day_num],user_answer)
	if day_dic[day_num] == user_answer:
		return 1
	else:
		return 0

if __name__ == '__main__':
	problem_list = [[1,1,2],[1900,2,28],[505,10,11],[2100,2,28],[8888,2,29],[1000,9,12],[4008,1,30],[9999,7,22],[2018,7,6],[1234,4,30]]
	score = 0
	for i in range(10):
		if checking_answer(problem_list[i][0],problem_list[i][1],problem_list[i][2],solution.your_answer(problem_list[i][0],problem_list[i][1],problem_list[i][2])) == 1:
			print(str(i+1)+"번 문제 통과 (number",str(i+1),"problem success)")
			score += 10
		else:
			print(str(i+1)+"번 문제 실패 (number",str(i+1),"problem fail)")
	print("점수:",str(score),"(score:",str(score)+")")