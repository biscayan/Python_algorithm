import copy
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# simulation
def fish_move():
    for fish in range(1,17):
        x, y, fdir = -1, -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == fish:
                    x, y, fdir = i, j, board[i][j][1]

        if fdir == -1:
            continue

        for i in range(8):
            if fdir+i < 8:
                ndir = fdir+i
                nx, ny = x+dx[ndir], y+dy[ndir]
            else:
                ndir = fdir+i-8
                nx, ny = x+dx[ndir], y+dy[ndir]
            if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0] != 100:
                board[x][y][1] = ndir
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                break       

# backtracking
def shark_move(sx,sy,sdir,eat):

    global answer, board

    fish_move()
    new_board = copy.deepcopy(board)
    candidate = []

    for i in range(1,4):
        nx, ny = sx+dx[sdir]*i, sy+dy[sdir]*i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0] > 0:
            candidate.append([board[nx][ny][0], nx, ny])

    if not candidate:
        answer = max(answer, eat)
        return 

    for fish, x, y in candidate:
        board = copy.deepcopy(new_board)
        board[x][y][0] = 100
        board[sx][sy][0] = 0
        shark_move(x,y,board[x][y][1],eat+fish)

if __name__ == '__main__':
    
    answer = 0
    dx, dy = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
    board = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        num_list = list(map(int, sys.stdin.readline().split()))
        for j in range(4):
            board[i][j].append(num_list[j*2])
            board[i][j].append(num_list[j*2+1]-1)
    fisrt_eat = board[0][0][0]
    board[0][0][0] = 100
    shark_move(0,0,board[0][0][1],fisrt_eat)
    print(answer)