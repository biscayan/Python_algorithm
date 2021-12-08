import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(sx,sy):
    global sheep, wolf, board

    sheep_cnt, wolf_cnt = 0, 0
    if board[sx][sy] == 'k':
        sheep_cnt += 1
    elif board[sx][sy] == 'v':
        wolf_cnt += 1
    board[sx][sy] = '#'
    queue = deque([(sx,sy)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C and board[nx][ny] != '#':
                if board[nx][ny] == 'k':
                    sheep_cnt += 1
                elif board[nx][ny] == 'v':
                    wolf_cnt += 1
                board[nx][ny] = '#'
                queue.append((nx,ny))
    
    if sheep_cnt > wolf_cnt:
        sheep += sheep_cnt
    else:
        wolf += wolf_cnt

if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split())
    board = list(list(sys.stdin.readline().strip()) for _ in range(R))
    sheep, wolf = 0, 0
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    for i in range(R):
        for j in range(C):
            if board[i][j] != '#':
                bfs(i,j)
    print(sheep, wolf)