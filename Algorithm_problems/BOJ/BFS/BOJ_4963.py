import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(a,b):

    global count

    queue = deque()

    ### 첫번째 노드 방문
    queue.append((a,b))
    board[a][b] = 0

    while queue:

        x, y = queue.popleft()

        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w and board[nx][ny] == 1:
                queue.append((nx,ny))
                board[nx][ny] = 0

    ### 섬을 발견하면 count +1
    count += 1

if __name__ == '__main__':

    ### 상 우상 우 우하 하 좌하 좌 좌상
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    while True:

        w, h = map(int, sys.stdin.readline().split())

        count = 0

        ### 더이상 입력이 없으면 while문 종료
        if w == 0 and h == 0:
            break
        
        board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:                    
                    bfs(i,j)

        print(count)