import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def DFS(vertex):

    print(vertex, end=' ')

    ### 방문여부 체크
    DFS_visited[vertex] = 1

    for v in graph[vertex]:
        if DFS_visited[v] == 0:
            DFS(v)


def BFS(start):

    queue = deque([])
    queue.append(start)

    while queue:

        v = queue.popleft()

        if BFS_visited[v] == 0:

            print(v, end=' ')

            ### 방문여부 체크
            BFS_visited[v] = 1

            for vertex in graph[v]:
                queue.append(vertex)


if __name__ == '__main__':

    N, M, V = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N+1)]
    DFS_visited = [0 for _ in range(N+1)]
    BFS_visited = [0 for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    ### 정점 번호가 작은 것부터 방문
    for vertex in graph:
        vertex.sort()

    DFS(V)
    print()
    BFS(V)