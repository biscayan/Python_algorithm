import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def Make_estate_num(sx,sy):

    house_count = 0

    queue = deque()

    house_map[sx][sy] = estate_num
    house_count += 1
    queue.append((sx,sy))

    while queue:

        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and house_map[nx][ny] == 1:
                house_map[nx][ny] = estate_num
                house_count += 1
                queue.append((nx,ny))

    estates.append(house_count)

if __name__ == '__main__':

    N = int(sys.stdin.readline())

    house_map = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
    
    estate_num = 2

    estates = []

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for i in range(N):
        for j in range(N):
            if house_map[i][j] == 1:
                Make_estate_num(i,j)
                estate_num += 1

    estates.sort()

    print(len(estates))

    for estate in estates:
        print(estate)