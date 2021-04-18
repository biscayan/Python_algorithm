import sys
from collections import deque
import copy

sys.stdin = open("input.txt", "r")

def Normal(array):

    queue = deque()

    visited = [[False] * N for _ in range(N)]

    count = 0

    for row in range(N):
        for col in range(N):
            if visited[row][col] == False:

                visited[row][col] = True
                queue.append((row,col))

                while queue:

                    x, y = queue.popleft()

                    for i in range(4):

                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0<=nx<N and 0<=ny<N and array[nx][ny] == array[x][y] and visited[nx][ny] == False:

                            visited[nx][ny] = True
                            queue.append((nx,ny))

                count += 1

    return count


def Abnormal(array):

    queue = deque()

    visited = [[False] * N for _ in range(N)]

    count = 0

    for row in range(N):
        for col in range(N):
            if visited[row][col] == False:

                visited[row][col] = True
                queue.append((row,col))

                while queue:

                    x, y = queue.popleft()

                    for i in range(4):

                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0<=nx<N and 0<=ny<N and array[nx][ny] == array[x][y] and visited[nx][ny] == False:

                            visited[nx][ny] = True
                            queue.append((nx,ny))

                count += 1

    return count


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    normal_board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    ### deepcopy normal board for making abnormal board
    abnormal_board = copy.deepcopy(normal_board)

    ### make red to green in the abnormal board
    for i in range(N):
        for j in range(N):
            if abnormal_board[i][j] == 'R':
                abnormal_board[i][j] = 'G'

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    noramal_result = Normal(normal_board)
    abnormal_result = Abnormal(abnormal_board)

    print(noramal_result, abnormal_result)