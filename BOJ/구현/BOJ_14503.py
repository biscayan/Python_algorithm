import sys
from collections import deque

'''
1. 현재 위치를 청소한다.

2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''

sys.stdin = open("input.txt")

# d=0:북, d=1:동, d=2:남, d=3:서

###왼쪽으로 방향 전환
def change_direc(d):

    ###북->서
    if d == 0:
        return 3
    ###동->북
    elif d == 1:
        return 0
    ###남->동
    elif d == 2:
        return 1
    ###서->남
    elif d == 3:
        return 2

###뒤로 후진
def move_back(d):

    ###북->남
    if d == 0:
        return 2
    ###동->서
    elif d == 1:
        return 3
    ###남->북
    elif d == 2:
        return 0
    ###서->동
    elif d == 3:
        return 1


def cleaning(r,c,d):

    ###현재 위치 청소
    result = 1

    ###청소를 한 곳은 숫자를 변경
    area_map[r][c] = 2

    queue = deque([[r,c]])

    while queue:

        #print(queue)

        ### y축방향(r), x축방향(c)
        y, x = queue.popleft()

        for i in range(4):

            d = change_direc(d)

            nx = x + dx[d]
            ny = y + dy[d]

            ###구역 안에 있고 청소를 하지 않았다면
            if 0<=nx<M and 0<=ny<N and area_map[ny][nx] == 0:
                
                ###청소
                result += 1
                area_map[ny][nx] = 2
                queue.append([ny,nx])

                break

            ###네 방향을 모두 확인했을 때
            if i == 3:

                nx = x + dx[move_back(d)]
                ny = y + dy[move_back(d)]

                queue.append([ny,nx])

                ###뒤로 후진하려 했지만 벽이라면 종료
                if area_map[ny][nx] == 1:
                    return result


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())    
    
    r, c, d = map(int, sys.stdin.readline().split())

    area_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  

    ###북동남서
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    print(cleaning(r,c,d))