import sys

sys.stdin = open("input.txt", "r")

def get_smallest_node():
    
    min_value = INF

    index = 0

    for i in range(1, n+1):
        ### 최소거리보다 짧으면서 방문한 적이 없을 때
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def simple_dijkstra(start):

    ### 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for node_info in graph[start]:
        next_node, cost = node_info[0], node_info[1]
        distance[next_node] = cost
    
    ### 시작 노드를 제외하여 n-1번 반복
    for _ in range(n-1):

        now = get_smallest_node()
        visited[now] = True

        ### now 노드와 연결된 다른 노드를 확인
        for node_info in graph[now]:
            cost = distance[now] + node_info[1]
            if cost < distance[node_info[0]]:
                distance[node_info[0]] = cost


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

    simple_dijkstra(start)
    
    for i in range(1, n+1):
        print("{}번 노드로 이동할 때의 거리 : ".format(i), distance[i])