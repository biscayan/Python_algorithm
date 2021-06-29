import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def maze_navi(sx, sy):

    queue = deque([(sx,sy)])

    while queue:

        x, y = queue.popleft()
        
        for i in range(4):

            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx,ny))

    return board[N-1][M-1]


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    # up right down left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    print(maze_navi(0,0))