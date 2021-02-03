import sys
import copy
from collections import deque

### pypy3은 통과, python3은 시간초과

sys.stdin = open("input.txt", "r")

### BFS
def Laboratory():

    global result

    ### 현재 board에서의 정답
    count = 0

    ### 맨 처음의 바이러스 위치를 담은 배열을 복사
    queue = deque(copy.deepcopy(virus_location))

    ### 현재 경우에서의 board
    array = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            array[i][j] = lab[i][j]

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            ### 바이러스 전염
            if 0<=nx<N and 0<=ny<M and array[nx][ny] == 0:
                array[nx][ny] = 2
                queue.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                count += 1

    ### 안전영역의 수를 update
    if count > result:
        result = count


### DFS
def Wall(lvl):

    ### 벽 3개를 모두 설치했을 때 탐색을 시작
    if lvl == 3:
        Laboratory()
        return

    ### 재귀적으로 모든 빈칸에 대하여 벽을 설치
    else:
        for i in range(N):
            for j in range(M):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    Wall(lvl+1)
                    lab[i][j] = 0


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = 0

    ### 맨 처음의 바이러스 위치 저장
    virus_location = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                virus_location.append((i,j))

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    Wall(0)

    print(result)