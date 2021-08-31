"""
아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
    - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def BFS(sx,sy):
    
    global answer

    size = 2
    eat = 0
    count = 0
    flag = False

    queue = deque([(sx,sy)])
    visited = [[False] * N for _ in range(N)]

    # 탐색에 문제가 없도록 시작 지점의 값을 0으로 변경
    board[sx][sy] = 0
    visited[sx][sy] = True

    while queue:
        # 좌상단의 물고기부터 먹어야하므로 정렬 진행
        queue = deque(sorted(queue))

        for _ in range(len(queue)):

            x, y = queue.popleft()

            if board[x][y] != 0 and board[x][y] < size:
    
                board[x][y] = 0
                eat += 1

                if eat == size:
                    size += 1
                    eat = 0

                # 다음 탐색을 위하여 큐와 방문여부 초기화
                queue = deque()
                visited = [[False] * N for _ in range(N)]

                answer = count
                flag = True

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and board[nx][ny] <= size:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

            # 조건에 만족하는 물고기를 먹었으므로 다른 방향의 물고기들을 탐색할 필요가 없음
            if flag:
                flag = False
                break

        count += 1
        
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx, dy = [-1,0,1,0], [0,-1,0,1]
    answer = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                BFS(i,j)

    print(answer)