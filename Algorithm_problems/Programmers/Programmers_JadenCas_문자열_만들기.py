def solution(s):
    answer = ''
    s_split = s.split(' ')
    for string in s_split:
        for i in range(len(string)):
            if string[i].isalpha() == True:
                if i == 0:
                    answer += string[i].upper()
                else:
                    answer += string[i].lower()
            else:
                answer += string[i]
        answer += ' '
    return answer[:-1]