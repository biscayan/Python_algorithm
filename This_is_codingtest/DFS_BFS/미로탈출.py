import sys
from collections import deque

sys.stdin = open("input.txt","r")

def BFS(n,m):

    queue = deque()
    queue.append((n,m))

    while queue:

        x, y = queue.popleft()

        ###상하좌우, 네 방향 탐색
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            ###시작지점은 탐색 제외
            if nx == 0 and ny == 0:
                continue
            
            ###다음지점이 범위 안에 있고 괴물이 었을 때,
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:

                ###직전 위치까지의 이동 횟수 + 1
                maze[nx][ny] = maze[x][y] + 1

                queue.append((nx,ny))
            
    destination = maze[N-1][M-1]
    
    return destination

        
if __name__ == '__main__':
    
    N, M = map(int, sys.stdin.readline().split())

    maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    ###북서남동
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    print(BFS(0,0))