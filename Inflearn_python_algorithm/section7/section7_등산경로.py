import sys

sys.stdin = open("input.txt", "r")

def climbing_path(x,y):

    global count

    if x == end_x and y == end_y:
        count += 1

    else:
        for i in range(4):

            nx = x + dx[i]  
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and path[nx][ny] > path[x][y] and visited[nx][ny] == False:
                visited[nx][ny] = True
                climbing_path(nx,ny)
                visited[nx][ny] = False


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    path = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    
    count = 0

    ### initialize start point
    start = 1000000
    start_x, start_y = 0,0

    ### initialize end point
    end = -1000000
    end_x, end_y = 0,0

    ### find start point and end point
    for i in range(N):
        for j in range(N):
            if path[i][j] < start:
                start = path[i][j]
                start_x, start_y = i, j

            if path[i][j] > end:
                end = path[i][j]
                end_x, end_y = i, j

    ### up right down left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    visited[start_x][start_y] = True

    climbing_path(start_x, start_y)

    print(count)