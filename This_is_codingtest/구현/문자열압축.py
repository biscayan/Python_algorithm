
def solution(s):

    ###answer를 최대값으로 초기화
    answer = len(s)
    
    if len(s) == 1:
        return 1

    for step in range(1,len(s)//2+1):
        
        ###압축된 sequence를 담을 변수 설정
        sequence = ''

        ###step 1->2->3...순서로 확인
        previous = s[0:step]
        
        count = 1

        for i in range(step,len(s),step):
            
            ###같다면 압축 횟수를 추가
            if previous == s[i:i+step]:
                count += 1

            else:
                if count >= 2:
                    sequence = sequence + str(count) + previous

                ###압축이 되지 않았을 때는 계수를 적지 않음
                else:
                    sequence = sequence + previous
                
                ###비교할 previous를 초기화
                previous = s[i:i+step]
                
                ###압축횟수를 초기화
                count = 1  

        ###남은 문자들을 처리
        if count >= 2:
            sequence = sequence + str(count) + previous
        else:
            sequence = sequence + previous

        answer = min(answer, len(sequence))

    return answer    


if __name__ == '__main__':

    ###test case1
    s = "aabbaccc"
    print(solution(s))

    ###test case2
    s = "ababcdcdababcdcd"
    print(solution(s))

    ###test case3
    s = "abcabcdede"
    print(solution(s))

    ###test case4
    s = "abcabcabcabcdededededede"
    print(solution(s))

    ###test case5
    s = "xababcdcdababcdcd"
    print(solution(s))