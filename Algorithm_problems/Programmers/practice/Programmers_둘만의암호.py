def solution(s, skip, index):
    answer = ''
    skip_list = []
    for sk in skip:
        skip_list.append(ord(sk))
    for alpha in s:
        al_num = ord(alpha)
        idx = index
        while idx != 0:
            if al_num+1 in skip_list:
                al_num += 1
                if al_num > 122:
                    al_num = (al_num%123) + 97
            else:
                al_num += 1
                if al_num > 122:
                    al_num = (al_num%123) + 97
                if al_num not in skip_list:
                    idx -= 1
        answer += chr(al_num)           
    return answer