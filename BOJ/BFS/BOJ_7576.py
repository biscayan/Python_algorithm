import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def Tomato(array):

    queue = deque()

    result = 0

    mature_count = 0

    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                mature_count += 1
                queue.append((i,j))

    ### 저장될 때부터 모든 토마토가 익어있는 경우 0을 출력
    if mature_count == M * N:
        return result

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and array[nx][ny] == 0:
                array[nx][ny] = 1
                day[nx][ny] = day[x][y] + 1
                queue.append((nx,ny))

    immature_count = 0

    for row in range(N):
        for col in range(M):

            if array[row][col] == 0:
                immature_count += 1

            if day[row][col] > result:
                result = day[row][col]

    ### 토마토가 모두 익을 때까지의 최소 날짜를 출력
    if immature_count == 0:
        return result

    ### 토마토가 모두 익지는 못하는 상황이면 -1을 출력
    else:
        result = -1
        return result


if __name__ == '__main__':

    M, N = map(int, sys.stdin.readline().split())

    storage = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    day = [[0] * M for _ in range(N)]

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    print(Tomato(storage))