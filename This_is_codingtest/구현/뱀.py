import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def turn(direction, C):

    if C == 'L':
        direction = (direction-1) % 4

    elif C == 'D':
        direction = (direction+1) % 4

    return direction


def snake():

    time = 0

    turn_idx = 0

    ### 뱀위 초기 위치
    x, y = 1, 1
    board[1][1] = 2

    direction = 0

    ### 뱀의 위치를 저장할 queue
    queue = deque()
    
    ### 뱀의 초기 위치 저장
    queue.append((x,y))

    while True:

        nx, ny = x+dx[direction], y+dy[direction]

        if 1<=nx<=N and 1<=ny<=N and board[nx][ny] != 2:
            
            ### 사과를 먹을 경우
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                queue.append((nx,ny))
                time += 1

            ### 사과를 먹지 않을 경우
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx,ny))
                px, py = queue.popleft()
                board[px][py] = 0
                time += 1

        else:
            time += 1
            break
        
        ### 방향 turn
        if turn_idx < L and time == turn_list[turn_idx][0]:
            direction = turn(direction, turn_list[turn_idx][1])
            turn_idx += 1

        ### 뱀위 위치 update
        x, y = nx, ny

    return time

if __name__ == '__main__':
    
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    board = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(K):
        r, c = map(int,sys.stdin.readline().split())
        ### 사과가 있는 위치를 표시
        board[r][c] = 1

    L = int(sys.stdin.readline())
    
    turn_list = []

    for _ in range(L):
        X, C = sys.stdin.readline().split()
        ### 방향이 바뀌어야 하는 초와 방향정보를 저장
        turn_list.append((int(X), C))

    ### right down left up
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    print(snake())