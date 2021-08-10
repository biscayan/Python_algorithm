import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(sx,sy):

    queue = deque([(sx,sy)])
    distance = [[0] * W for _ in range(H)]
    
    while queue:
        x, y = queue.popleft()
        # end point
        if x == C_location[1][0] and y == C_location[1][1]:
            return distance[x][y] -1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # before changing the direction
            while 0<=nx<H and 0<=ny<W and board[nx][ny] != '*': 
                if distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx,ny))
                nx, ny = nx+dx[i], ny+dy[i]

if __name__ == '__main__':
    W, H = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(H)]

    # up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    C_location = []

    for i in range(H):
        for j in range(W):
            if board[i][j] == 'C':
                C_location.append((i,j))

    print(bfs(C_location[0][0], C_location[0][1]))