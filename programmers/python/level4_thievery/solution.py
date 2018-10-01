def solution(money):
    
    answer = 0
    size_h = len(money)
    if size_h == 3:
        return max(money)
    else:
        for i in range(3):
            std_idx = (size_h - i)%size_h
            another_list = money[(std_idx+2)%size_h:(std_idx+2)%size_h + size_h-3]
            size_another = len(another_list)
            another_cal_value = []
            if (size_another == 0) or (size_another == 1) or (size_another == 2):
                answer = max(answer, money[std_idx] + max(another_list))
            elif size_another == 3:
                answer = max(answer, money[std_idx] + max(another_list[0]+another_list[2], another_list[1]))
            else:
                for i, v in enumerate(another_list):
                    if (i == 0) or (i == 1):
                        another_cal_value.append(v)
                    elif i == 2:
                        another_cal_value.append(another_cal_value[0] + v)
                    else:
                        another_cal_value.append(v + max(another_cal_value[i-2],another_cal_value[i-3]))
                answer = max(answer, money[std_idx] + max(another_cal_value[-1], another_cal_value[-2]))
    return answer
