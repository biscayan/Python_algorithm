import sys

sys.stdin = open("input.txt","r")

def DFS(x, y):

    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    else:
        ###구멍이 뚫려있고 방문하지 않은 경우
        if ice_map[x][y] == 0 and visited[x][y] == False:

            visited[x][y] = True
            
            ###상하좌우 탐색
            DFS(x-1,y)
            DFS(x,y-1)
            DFS(x+1,y)
            DFS(x,y+1)

            return True

        return False


if __name__ == '__main__':
    
    N, M = map(int, sys.stdin.readline().split())

    ice_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    visited = [list([False] * M) for _ in range(N)]

    count = 0
    
    for i in range(N):
        for j in range(M):
            if DFS(i,j) == True:
                count += 1

    print(count)