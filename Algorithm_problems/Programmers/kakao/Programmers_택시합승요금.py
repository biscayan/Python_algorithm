# floyd warshall algorithm
def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

    # undirected graph
    for fare in fares:
        start, end, cost = fare
        graph[start][end] = cost
        graph[end][start] = cost

    for i in range(1,n+1):
        graph[i][i] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]

    answer = INF
    for i in range(1,n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])

    return answer