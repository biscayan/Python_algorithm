import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def safe_area(height, array):

    count = 0

    queue = deque()

    visited = [[False] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if array[row][col] > height and visited[row][col] == False:
                
                visited[row][col] = True
                queue.append((row,col))

                while queue:

                    x, y = queue.popleft()

                    for i in range(4):

                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N and array[nx][ny] > height and visited[nx][ny] == False:
                            
                            visited[nx][ny] = True
                            queue.append((nx,ny))
                count += 1

    return count

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    area_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ### initialize the min height and max height
    min_height = 101
    max_height = 0

    result = 0

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    ### find the min height and max height in the map
    for i in range(N):
        for j in range(N):
            if area_map[i][j] > max_height:
                max_height = area_map[i][j]

            if area_map[i][j] < min_height:
                min_height = area_map[i][j]        

    for k in range(min_height, max_height+1):
        
        areas = safe_area(k, area_map)

        if areas > result:
            result = areas

    print(result)