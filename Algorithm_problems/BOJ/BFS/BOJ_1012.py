import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(sy, sx):
    queue = deque([(sy,sx)])
    graph[sy][sx] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    # up right down left
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    for _ in range(T):
        count = 0
        M, N, K = map(int, sys.stdin.readline().split())
        graph = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            graph[Y][X] = 1

        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    bfs(i,j)
                    count += 1

        print(count)