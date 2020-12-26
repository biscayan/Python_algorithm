import sys
from collections import deque

sys.stdin = open("input.txt","r")

def turn_left(d):

    if d == 0:
        return 3
    elif d == 3:
        return 2
    elif d ==2:
        return 1
    elif d == 1:
        return 0

def move_back(d):

    if d == 0:
        return 2
    elif d == 3:
        return 1
    elif d ==2:
        return 0
    elif d == 1:
        return 3

def Game(a,b,d):

    answer = 0

    queue = deque([[a,b]])

    ###초기장소
    visited[a][b] = True
    answer += 1

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):

            d = turn_left(d)

            nx = x + dx[d]
            ny = y + dy[d]

            ###이동 가능 조건
            ###(1)다음 이동 장소가 map범위안에 있고
            ###(2)다음 이동 장소를 방문한 적이 없고
            ###(3)다음 이동 장소가 바다가 아니여야 함
            if 0<=nx<=N and 0<=ny<=M and visited[nx][ny] == False and game_map[nx][ny] == 0:

                visited[nx][ny] = True
                answer += 1
                queue.append([nx,ny])

                break
            
            ###네 방향을 모두 확인했을 때,
            if i == 3:

                nx = x + dx[move_back(d)]
                ny = y + dy[move_back(d)]

                queue.append([nx,ny])

                ###후진을 했지만 바다라서 더 이상 이동 할 수 없다면 종료
                if game_map[nx][ny] == 1:
                    return answer

if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())
    A, B, d = map(int, sys.stdin.readline().split())

    game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ### 북동남서
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    visited = [[False] * M for _ in range(N)]

    print(Game(A, B, d))