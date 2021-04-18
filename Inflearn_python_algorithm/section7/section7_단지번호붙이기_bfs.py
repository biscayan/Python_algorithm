import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def house_grouping(array):

    queue = deque()

    for row in range(N):
        for col in range(N):
            if array[row][col] == 1 and visited[row][col] == False:
                
                ### The first house of the grouping
                visited[row][col] = True
                count = 1
                queue.append((row,col))

                while queue:

                    x, y = queue.popleft()

                    for i in range(4):
                        
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N and array[nx][ny] == 1 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            count += 1
                            queue.append((nx,ny))

                count_list.append(count)
    
    count_list.sort()
    
    grouping_num = len(count_list)

    print(grouping_num)
    
    for houses in count_list:
        print(houses)

if __name__ == '__main__':
    
    N = int(sys.stdin.readline())

    house_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    count_list = []

    house_grouping(house_map)