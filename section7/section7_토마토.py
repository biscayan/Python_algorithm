import sys
from collections import deque

sys.stdin = open("input.txt","r")

def Tomato(storage, day):

    queue = deque()

    result = 0

    mature_count = 0

    for row in range(M):
        for col in range(N):

            ### 현재 익어있는 토마토
            if storage[row][col] == 1:

                mature_count += 1
                queue.append((row,col))

    ### 토마토들이 모두 익어있는 상태라면 0을 리턴, 함수 종료    
    if mature_count == N * M:
        return result

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            ### 다음 이동 위치가 범위 안에 있고 그 토마토가 익어져야 하는 경우
            if 0<=nx<M and 0<=ny<N and storage[nx][ny] == 0:
                
                ### 창고에는 익은 것으로 표시
                storage[nx][ny] = 1
                ### 하루가 지남
                day[nx][ny] = day[x][y] + 1
                queue.append((nx,ny))

    immature = False

    for i in range(M):
        for j in range(N):
            if storage[i][j] == 0:
                immature = True
                break
    
    ### 창고에 익지 않은 토마토가 남아 있는 경우 -1을 리턴
    if immature == True:
        result = -1
        
    ### 토마토가 모두 익었으면 토마토가 익는데 필요한 최소 일수를 리턴    
    else:
        for i in range(M):
            for j in range(N):
                if day[i][j] > result:
                    result = day[i][j]

    return result


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    ### 토마토 창고
    storage = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    ### 토마토를 익히는 일수를 저장
    day = [[0] * N for _ in range(M)]

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    print(Tomato(storage, day))