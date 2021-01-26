import sys

sys.stdin = open("input.txt", "r")

def maze_path(x,y):

    global count

    if x == N-1 and y == N-1:
        count += 1

    else:
        for i in range(4):

            nx = x + dx[i] 
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and maze[nx][ny] == 0:

                maze[nx][ny] = 1
                maze_path(nx, ny)
                ### 벽을 다시 통로로 만들어 줘야 다음탐색 때 방문을 할 수 있음
                maze[nx][ny] = 0

if __name__ == '__main__':
    
    N = int(sys.stdin.readline())
    maze = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    ### 상 우 하 좌
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    count = 0

    maze[0][0] = 1

    maze_path(0,0)

    print(count)