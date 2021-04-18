import heapq
import sys

sys.stdin = open("input.txt", "r")

def telegram(start):

    queue = []

    heapq.heappush(queue, (0, start))

    ### 시작지점은 거리가 0
    distance[start] = 0

    while queue:

        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for node in graph[now]:

            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue,(cost, node[0]))

    count = 0
    time = 0
    
    for d in distance:
        if d != INF:
            count += 1
            time = max(time, d)

    print(count-1, time)


if __name__ == '__main__':

    N, M, C = map(int, sys.stdin.readline().split())

    INF = int(1e9)

    graph = [[] for _ in range(N+1)]

    distance = [INF] * (N+1)

    for _ in range(M):
        X, Y, Z = map(int, sys.stdin.readline().split())
        graph[X].append((Y,Z))

    telegram(C)