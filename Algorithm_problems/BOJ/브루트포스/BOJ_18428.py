import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")

def avoid_supervision(graph, teacher):
    for tx, ty in teacher:
        for i in range(4):
            nx, ny = tx+dx[i], ty+dy[i]
            while 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 'S':
                    return False
                elif graph[nx][ny] == 'O':
                    break
                nx, ny = nx+dx[i], ny+dy[i]

    return True

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    graph = [sys.stdin.readline().split() for _ in range(N)]

    dx, dy = [-1,0,1,0], [0,1,0,-1]
    empty, teacher = [], []
    avoid = False

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                empty.append((i, j))
            elif graph[i][j] == 'T':
                teacher.append((i, j))

    blocks = list(combinations(empty,3))

    for block in blocks:
        for i in range(3):
            x, y = block[i][0], block[i][1]
            graph[x][y] = 'O'
        if avoid_supervision(graph, teacher):
            avoid = True
            break
        for i in range(3):
            x, y = block[i][0], block[i][1]
            graph[x][y] = 'X'

    if avoid:
        print("YES")
    else:
        print("NO")