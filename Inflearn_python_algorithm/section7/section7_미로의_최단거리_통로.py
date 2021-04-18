import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def maze_path(array, start_x, start_y):

    queue = deque()

    queue.append((start_x, start_y))

    visited[start_x][start_y] = True

    while queue:

        x, y = queue.popleft()
        
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            ### 범위 안에 있으며, 방문하지 않았고, 다음 이동 위치가 벽이 아닐 때,
            ### 범위 안에 있는지를 먼저 살펴봐야 오류가 안남, 제일 왼쪽에 있는 조건의 논리구조를 따지기 때문! 
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and array[nx][ny] == 0:
                visited[nx][ny] = True
                move_sum[nx][ny] = move_sum[x][y] + 1
                queue.append((nx,ny))

    if move_sum[N-1][N-1] == 0:
        print(-1)
    else:
        print(move_sum[N-1][N-1])

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    maze = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    ### 방문여부 체크
    visited = [[False] * N for _ in range(N)]
    
    ### 현재의 위치까지 이동횟수를 저장
    move_sum = [[0] * N for _ in range(N)]

    ### 상 우 하 좌
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    maze_path(maze, 0, 0)