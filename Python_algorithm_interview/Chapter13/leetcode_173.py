import heapq

def networkDelayTime(times, n, k) -> int:
    graph = [[] for _ in range(n+1)]
    for u, v, w in times:
        graph[u].append((v,w))

    INF = 1e9
    distance = [INF] * (n+1)
    distance[k] = 0

    heap = []
    heapq.heappush(heap,(k, distance[k]))

    while heap:
        cur, cost = heapq.heappop(heap)
        if distance[cur] < cost:
            continue
        for nxt in graph[cur]:
            if distance[nxt[0]] > nxt[1]+cost:
                distance[nxt[0]] = nxt[1]+cost
                heapq.heappush(heap,(nxt[0],distance[nxt[0]]))
    
    if INF in distance[1:]:
        return -1
    else:
        return max(distance[1:])