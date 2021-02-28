import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def contagion(lab):

    array = []

    for i in range(N):
        for j in range(N):
            if lab[i][j] != 0:
                array.append((lab[i][j],0,i,j))

    ### virus번호를 기준으로 오름차순 정렬
    array.sort()

    queue = deque(array)

    while queue:

        virus, sec, x, y = queue.popleft()

        ### S초가 지나면 중단
        if sec == S:
            break 

        for i in range(4):

            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<N and 0<=ny<N and lab[nx][ny] == 0:
                lab[nx][ny] = virus
                queue.append((virus,sec+1,nx,ny))

    result = lab[X-1][Y-1]

    return result


if __name__ == '__main__':

    ### input
    N, K = map(int, sys.stdin.readline().split())
    laboratory = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    S, X, Y = map(int, sys.stdin.readline().split())

    ### up right down left
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    print(contagion(laboratory))