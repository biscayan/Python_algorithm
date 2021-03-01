import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def find_city(start):

    distance = [-1] * (N+1)

    queue = deque()

    ### 시작지점 방문 처리
    queue.append(start)
    distance[start] = 0

    while queue:

        now = queue.popleft()

        for node in graph[now]:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                queue.append(node)
    
    flag = False

    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
            flag = True

    ### 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1 출력
    if flag == False:
        print(-1)


if __name__ == '__main__':

    ### N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발 도시의 번호
    N, M, K, X = map(int, sys.stdin.readline().split())

    visited = [False] * (N+1)
    graph = [[ ] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)

    find_city(X)