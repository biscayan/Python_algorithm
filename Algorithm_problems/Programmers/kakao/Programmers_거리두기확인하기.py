from collections import deque

def BFS(sx, sy, waiting):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    queue = deque()
    queue.append((sx,sy))
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[sx][sy] = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if visited[nx][ny] == 0 and (abs(sx - nx) + abs(sy - ny) <= 2):
                    if waiting[nx][ny] == 'O':
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
                    elif waiting[nx][ny] == 'P':
                        return False

    return True


def solution(places):
    answer = []
    for place in places:
        check = True
        waiting = []
        for line in place:
            waiting.append(list(line))
        for i in range(5):
            for j in range(5):
                if waiting[i][j] == 'P':
                    if not BFS(i,j,waiting):
                        check = False
                        break

        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer