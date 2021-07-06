import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def knight_move(sx, sy, count):

    queue = deque([(sx,sy,count)])

    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[sx][sy] = True

    while queue:

        x, y, cnt = queue.popleft()
        
        if x == final_x and y == final_y:
            return cnt

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny] == False:
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = True

if __name__ == '__main__':
    # 좌상 우상 우하 좌하
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    T = int(sys.stdin.readline())

    for _ in range(T):
        l = int(sys.stdin.readline())
        start_x, start_y = map(int, sys.stdin.readline().split())
        final_x, final_y = map(int, sys.stdin.readline().split())
        print(knight_move(start_x, start_y, 0))