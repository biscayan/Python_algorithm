import sys

sys.stdin = open("input.txt", "r")

def floyd(graph):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for r in range(n):
        for c in range(n):
            if graph[r][c] == INF:
                graph[r][c] = 0
            print(graph[r][c], end=' ')
        print()


if __name__ == '__main__':

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    INF = 1e9
    graph = [[INF for _ in range(n)] for _ in range(n)] 

    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        ### 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
        graph[start-1][end-1] = min(graph[start-1][end-1], cost)

    floyd(graph)