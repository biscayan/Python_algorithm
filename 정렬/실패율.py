def solution(N, stages):
    
    array = []

    players = len(stages)

    for stage in range(1, N+1):

        ### 현재 stage에서 실패한 player의 수
        count_fail = stages.count(stage)

        ### player들이 이전에 모두 실패하여 현재 stage에 도전할 player가 없을 때
        if players == 0:
            fail_rate = 0.0
            array.append((stage, fail_rate))

        ### 다음 stage로 넘어가기 전에 실패한 player의 수는 빼줌
        else:
            fail_rate = count_fail / players
            players -= count_fail
            array.append((stage, fail_rate))

    ### stage의 실패율을 기준으로 내림차순 정렬
    sorted_array = sorted(array, key = lambda x:-x[1])

    answer  = []

    ### stage의 단계만 담음
    for i in range(len(sorted_array)):
        answer.append(sorted_array[i][0])

    return answer

if __name__ == '__main__':

    ### test case1
    N = 5
    stages = [2,1,2,6,2,4,3,3]
    print(solution(N, stages))

    ### test case2
    N = 4
    stages = [4,4,4,4,4]
    print(solution(N, stages))