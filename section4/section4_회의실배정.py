import sys

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())

meeting = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start,end))

###회의가 끝나는 시간을 기준으로 정렬해야함
meeting.sort(key = lambda time:time[1])

#print(meeting)

answer = 1

curr = meeting[0]

for i in range(1,n):
    ###다음시작시간 >= 현재의 끝나는시간
    if meeting[i][0] >= curr[1]:
        answer += 1
        curr = meeting[i]
        
print(answer)