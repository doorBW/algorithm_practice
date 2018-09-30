def solution(n, arr1, arr2):
    answer = []
    decode_arr1 = []
    decode_arr2 = []
    tmp_str = ''
    tmp_answer = ''
    for i in arr1:
        tmp_str = str(bin(i))[2:]
        while(len(tmp_str) < n):
            tmp_str = '0'+tmp_str
        tmp_str = tmp_str.replace('0',' ')
        tmp_str = tmp_str.replace('1','#')
        decode_arr1.append(tmp_str)
    for i in arr2:
        tmp_str = str(bin(i))[2:]
        while(len(tmp_str) < n):
            tmp_str = '0'+tmp_str
        tmp_str = tmp_str.replace('0',' ')
        tmp_str = tmp_str.replace('1','#')
        decode_arr2.append(tmp_str)
    
    for i in range(n):
        for j in range(n):
            if (decode_arr1[i][j] == '#') or (decode_arr2[i][j] == '#'):
                tmp_answer += '#'
            else:
                tmp_answer += ' '
        answer.append(tmp_answer)
        tmp_answer = ''
    return answer
