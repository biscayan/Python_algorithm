import heapq
import sys

sys.stdin = open("input.txt", "r")

def advanced_dijkstra(start):

    queue = []

    ### (거리, 노드번호)를 queue에 저장
    heapq.heappush(queue,(0,start))

    distance[start] = 0

    while queue:
        
        dist, now = heapq.heappop(queue)
        
        ### now 노드가 처리된 적이 있다면 무시함
        if distance[now] < dist:
            continue
        
        ### now 노드와 연결된 다른 노드를 확인
        for node_info in graph[now]:
            cost = dist + node_info[1]
            if cost < distance[node_info[0]]:
                distance[node_info[0]] = cost
                heapq.heappush(queue,(cost, node_info[0]))


if __name__ == '__main__':

    ### n : 노드의 수 / m : 간선의 수
    n, m = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline())

    INF = int(1e9)

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    distance = [INF] * (n+1)

    for _ in range(m):
        ### a번 노드에서 b번 노드로 가는 비용이 c
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b,c))

    advanced_dijkstra(start)

    for i in range(1, n+1):
        print("{}번 노드로 이동할 때의 거리 : ".format(i), distance[i])