import sys

sys.stdin = open("input.txt", "r")

def floyd_warshall(graph):

    ### 플로이드 워셜 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    ### 그래프 출력
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == INF:
                print("I", end=' ')
            else:
                print(graph[i][j], end=' ')

        print()


if __name__ == '__main__':

    INF = int(1e9)

    ### 노드의 개수
    n = int(sys.stdin.readline())
    ### 간선의 개수
    m = int(sys.stdin.readline())

    graph = [[INF] * (n+1) for _ in range(n+1)]

    ### 자기 자신으로 이동하는 경우는 비용을 0으로 초기화
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start][end] = cost

    floyd_warshall(graph)