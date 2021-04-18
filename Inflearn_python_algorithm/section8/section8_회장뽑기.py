import sys

sys.stdin = open("input.txt", "r")

def Select_president(array):

    candidate_score = 50
    mamber_list = []
    candidate_list = []

    ### 플로이드 워셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                array[i][j] = min(array[i][j], array[i][k]+array[j][k])

    ### 가까운 정도를 계산하기 위하여 50을 0으로 바꿔줌
    for i in range(n+1):
        for j in range(n+1):
            if array[i][j] == 50:
                array[i][j] = 0
    
    ### 회원번호와 회원점수를 저장
    for member_num in range(1,n+1):
        score = max(array[member_num])
        mamber_list.append((member_num,score))
        candidate_score = min(score, candidate_score)

    ### 회원들 중에서 후보들을 저장
    for member in mamber_list:
        if member[1] == candidate_score:
            candidate_list.append(member[0])

    candidate_count = len(candidate_list)

    print(candidate_score, candidate_count)
    
    for candidate in candidate_list:
        print(candidate, end=' ')


if __name__ == '__main__':

    n = int(sys.stdin.readline())

    dp_table = [[50] * (n+1) for _ in range(n+1)]
    
    while True:
        
        member1, member2 = map(int, sys.stdin.readline().split())
        
        ### 무방향그래프
        dp_table[member1][member2] = 1
        dp_table[member2][member1] = 1

        if member1 == -1 and member2 == -1:
            break

    Select_president(dp_table)