import sys
from collections import deque

# pypy3은 통과, python3은 시간초과
sys.stdin = open("input.txt", "r")

# BFS
def Laboratory():

    global result

    # 현재 경우에서의 board
    # 이중for문이 copy.deepcopy보다 빠름 2700ms -> 1200ms
    board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board[i][j] = lab[i][j]

    # 전염 이전의 바이러스 위치
    queue = deque(virus_location)
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):    
            nx, ny = x + dx[i], y + dy[i]
            # 바이러스 전염
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx,ny))

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                count += 1

    result = max(count, result)

# DFS
def Wall(lvl):
    # 벽 3개를 모두 설치했을 때 탐색을 시작
    if lvl == 3:
        Laboratory()
        return

    # 재귀적으로 모든 빈칸에 대하여 벽을 설치
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
    virus_location = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                virus_location.append((i,j))

    # up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    Wall(0)
    print(result)