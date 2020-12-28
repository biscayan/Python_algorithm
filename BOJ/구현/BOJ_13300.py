import sys

sys.stdin = open("input.txt", "r")


N, K = map(int, sys.stdin.readline().split())

answer = 0

###1~6학년 [여자,남자] 7x2행렬
student_list = [[0,0] for _ in range(7)]

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())

    student_list[Y][S] += 1

for i in range(2):
    for j in range(len(student_list)):
        ###K명씩 배정
        answer += student_list[j][i] // K
        ###남는 인원이 존재하면 +1
        if student_list[j][i] % K:
            answer += 1

print(answer)