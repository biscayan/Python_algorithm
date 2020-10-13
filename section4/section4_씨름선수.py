import sys

sys.stdin = open("input.txt","r")

player_list = []

N = int(sys.stdin.readline())

for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())
    player_list.append((h,w))

player_list.sort(reverse=True)

for i in range(1,N):
    for j in range(i):
        ###기준미달의 후보들을 제거
        if player_list[i][1] < player_list[j][1]:
            N-=1
            break
print(N)