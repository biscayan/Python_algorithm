import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def island_country(array):

    queue = deque()

    count = 0

    for row in range(N):
        for col in range(N):
            if array[row][col] == 1:

                array[row][col] = 0
                queue.append((row,col))

                while queue:

                    x, y = queue.popleft()

                    for i in range(8):
                        
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N and array[nx][ny] == 1:

                            array[nx][ny] = 0
                            queue.append((nx,ny))
                
                count += 1

    print(count)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    island_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ### 상 상우 우 하우 하 하좌 좌 상좌
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    island_country(island_map)