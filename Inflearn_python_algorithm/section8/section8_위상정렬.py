import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def Topological_sort(graph, degree):

    queue = deque()

    ### 진입차수가 0인것부터 우선적으로 처리함
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        
        node = queue.popleft()
        
        print(node, end=' ')

        for i in range(1, N+1):
            if graph[node][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)


if __name__ == '__main__':

    N, M = map(int, sys.stdin.readline().split())

    ### 단방향 그래프
    graph = [[0] * (N+1) for _ in range(N+1)]

    ### 진입차수의 개수를 저장 
    degree = [0] * (N+1)

    for i in range(M):

        start, end = map(int, sys.stdin.readline().split())
        graph[start][end] = 1
        degree[end] += 1

    Topological_sort(graph, degree)