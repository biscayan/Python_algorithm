### pypy3로는 통과, python3은 시간초과

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(x,y):

    queue = deque()
    queue.append([x,y])
    
    union = []
    union.append([x,y])

    visited[x][y] = True

    while queue:

        x,y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            ### 다음 위치가 범위 안에 있으면서 방문하지 않았을 경우
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                if L <= abs(board[nx][ny] - board[x][y]) <= R:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    union.append([nx,ny])

    return union


if __name__ == '__main__':

    N, L, R = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ### 상우하좌
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    answer = 0

    while True:
        
        ### 방문여부 체크
        visited = [[False] * N for _ in range(N)]

        ### 연합이 생겼는지를 확인
        flag = False

        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:

                    sub_union = bfs(i,j)

                    ### 연합이 생김
                    if len(sub_union) > 1:

                        num_sum = 0

                        for sub in sub_union:
                            num_sum += board[sub[0]][sub[1]]

                        ### 인구 수 계산
                        avg = num_sum // len(sub_union)

                        for sub in sub_union:
                            board[sub[0]][sub[1]] = avg

                        flag = True

        ### 연합이 생기지 않았으면 반복을 중단시킴
        if not flag:
            break  
        
        ### 인구이동일의 수를 증가
        answer += 1 

    print(answer) 