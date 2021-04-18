import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def apple_tree(array):

    count = 0
    lvl = 0

    half_N = N//2
    
    queue = deque()

    queue.append((half_N, half_N))

    ### 농장의 정중앙에서부터 탐색 시작
    check[half_N][half_N] = True
    count += array[half_N][half_N]
    
    while queue:

        if lvl == half_N:
            break
        
        for _ in range(len(queue)):

            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if check[nx][ny] == False:

                    count += array[nx][ny]
                    check[nx][ny] = True
                    
                    queue.append((nx,ny))
                
        lvl += 1
        
    print(count)


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

    check = [[False] * N for _ in range(N)]

    ### 상 우 하 좌
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    apple_tree(farm)