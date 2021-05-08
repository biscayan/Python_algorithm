import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")

def avoid_supervision(graph, teacher):

    for t_location in teacher:

        t_x, t_y = t_location[0], t_location[1]

        ### 상 탐색
        while t_x > 0:
            t_x -= 1
            if graph[t_x][t_y] == 'S':
                return False
            elif graph[t_x][t_y] == 'O':
                break

        t_x, t_y = t_location[0], t_location[1]
        
        ### 하 탐색
        while t_x < N-1:
            t_x += 1
            if graph[t_x][t_y] == 'S':
                return False
            elif graph[t_x][t_y] == 'O':
                break
        
        t_x, t_y = t_location[0], t_location[1]

        ### 좌 탐색
        while t_y > 0:
            t_y -= 1
            if graph[t_x][t_y] == 'S':
                return False
            elif graph[t_x][t_y] == 'O':
                break
        
        t_x, t_y = t_location[0], t_location[1]

        ### 우 탐색
        while t_y < N-1:
            t_y += 1
            if graph[t_x][t_y] == 'S':
                return False
            elif graph[t_x][t_y] == 'O':
                break

    return True


if __name__ == '__main__':

    N = int(sys.stdin.readline())

    empty, teacher = [], []

    flag = False

    graph = [sys.stdin.readline().split() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                empty.append((i, j))
            elif graph[i][j] == 'T':
                teacher.append((i, j))

    block = list(combinations(empty,3))

    for candidate in block:
        for i in range(3):
            x, y = candidate[i][0], candidate[i][1]
            graph[x][y] = 'O'

        if avoid_supervision(graph, teacher) == True:
            flag = True
            break

        for i in range(3):
            x, y = candidate[i][0], candidate[i][1]
            graph[x][y] = 'X'

    if flag == True:
        print("YES")
    else:
        print("NO")