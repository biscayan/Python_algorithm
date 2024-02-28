def solution(keymap, targets):
    answer = []
    dict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dict:
                dict[key[i]] = i+1
            else:
                if i+1 < dict[key[i]]:
                    dict[key[i]] = i+1
    
    for target in targets:
        num = 0
        flag = True
        for t in target:
            if t not in dict.keys():
                answer.append(-1)
                flag = False
                break
            else:
                num += dict[t]
        if flag:
            answer.append(num)
                
    return answer