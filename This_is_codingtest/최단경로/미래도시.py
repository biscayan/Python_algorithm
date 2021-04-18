import sys

sys.stdin = open("input.txt", "r")

### Floyd Warshall algorithm
def future_city(x, k):

    for c in range(1, N+1):
        for a in range(1, N+1):
            for b in range(1, N+1):
                graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

    ### 1 -> K -> X 순서로 이동
    result = graph[1][k] + graph[k][x]

    if result < INF:
        return result
    else:
        return -1


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    INF = int(1e9)

    graph = [[INF] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        city1, city2 = map(int, sys.stdin.readline().split())
        graph[city1][city2] = 1
        graph[city2][city1] = 1

    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                graph[i][j] = 0

    X, K = map(int, sys.stdin.readline().split())
    
    print(future_city(X, K))